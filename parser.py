import mimetypes
import pandas as pd

class Parser:
    def __init__(self) -> None:
        self.df = pd.DataFrame()
        self.mimetype_input = ""
        self.mimetype_output = ""
        print("Started converting data.")

    # Ingests Data (Import from CSV / JSON)
    def ingest_data(self, filename):
        self.mimetype_input = mimetypes.guess_type(filename)[0]
        match self.mimetype_input:
            case 'application/json':
                self.df = pd.read_json(filename)
            case 'text/csv':
                self.df = pd.read_csv(filename, delimiter=";")
            case other:
                raise Exception("Invalid input file type.")

    # Extracts columns in place
    def extract_columns(self, columns):
        _temp_df = self.df
        self.df = _temp_df.filter(items=columns)

    # Combine columns into one
    def combine_columns(self, column_one, column_two, final_column):
        self.df[final_column] = self.df[column_one].astype('str') + self.df[column_two].astype('str').str.zfill(2)

    # Bottles Data (Export to CSV / JSON)
    # Just provide correct filename
    def bottle_data(self, filename):
        self.mimetype_output = mimetypes.guess_type(filename)[0]
        match self.mimetype_output:
            case 'application/json':
                self.df.to_json(filename, orient="records")
            case 'text/csv':
                self.df.to_csv(filename, index=False)
            case other:
                raise Exception("Invalid output file type.")

    def __del__(self):
        print("Finished with conversion and filtering.")