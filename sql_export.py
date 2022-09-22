import math

class SQLExport:
    def __init__(self, data) -> None:
        self.data = data
        self.template = """
CREATE TABLE IF NOT EXISTS addresses(postleitzahl integer NOT NULL , plz_zz integer NOT NULL , ortbez18 text NOT NULL , kanton varchar(2) NOT NULL , sprachcode integer NOT NULL , geokoordinaten text ,plz6 integer NOT NULL);

INSERT INTO addresses(POSTLEITZAHL,PLZ_ZZ,ORTBEZ18,KANTON,SPRACHCODE,Geokoordinaten,PLZ6) VALUES
        """

    def __append_line(self, line):
        self.template += "\n" + line

    def __safe_string(self, string):
        return string.replace("'", "''")

    def export(self):
        for i, item in enumerate(self.data):
            plz = item["POSTLEITZAHL"]
            plz_zz = item["PLZ_ZZ"]
            location = self.__safe_string(item["ORTBEZ18"])
            canton = item["KANTON"]
            lang = item["SPRACHCODE"]
            coords = "NULL" if len(str(item["Geokoordinaten"])) < 4 else "'" + item["Geokoordinaten"] + "'"
            plz6 = item["PLZ6"]

            if i == len(self.data)-1: # last line
                self.__append_line(f"({plz},{plz_zz},'{location}','{canton}',{lang},{coords},{plz6});")
            else:
                self.__append_line(f"({plz},{plz_zz},'{location}','{canton}',{lang},{coords},{plz6}),")

    def save(self, filename):
        with open(filename, 'w+') as f:
            f.write(self.template)
            f.close()