import base64
from zipfile import ZipFile
from parser import Parser
from downloader import Downloader

if __name__=="__main__":

    source_url=base64.b64decode("aHR0cHM6Ly9zd2lzc3Bvc3Qub3BlbmRhdGFzb2Z0LmNvbS9leHBsb3JlL2RhdGFzZXQvcGx6X3ZlcnplaWNobmlzX3YyL2Rvd25sb2FkLz9mb3JtYXQ9Y3N2JnRpbWV6b25lPUV1cm9wZS9CZXJsaW4mbGFuZz1kZSZ1c2VfbGFiZWxzX2Zvcl9oZWFkZXI9dHJ1ZSZjc3Zfc2VwYXJhdG9yPSUzQg==").decode("utf-8")

    source_file="plz.csv"
    dest_files=["plz_extracted.csv","plz_extracted.json"]

    ################################################

    # Download new Dataset
    downloader = Downloader(source_url)
    downloader.get()
    downloader.save(source_file)

    ################################################

    parser = Parser()

    # Import File
    parser.ingest_data(source_file)

    # Filters

    ## Filter Columns
    parser.extract_columns(["POSTLEITZAHL", "PLZ_ZZ", "ORTBEZ18", "KANTON", "SPRACHCODE", "Geokoordinaten"])

    ## Combine Columns
    parser.combine_columns(column_one="POSTLEITZAHL", column_two="PLZ_ZZ", final_column="PLZ6")

    # Export File
    with ZipFile('plz_extracted.zip', 'w') as myzip:
        for dest_file in dest_files:
            parser.bottle_data(dest_file)
            myzip.write(dest_file)

