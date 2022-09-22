import requests

class Downloader:
    def __init__(self, url) -> None:
        self.url = url
        self.response = None
        print("Started downloading data.")
        
    def get(self):
        self.response = requests.get(self.url)

    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(self.response.text)

    def __del__(self):
        print("Finished downloading data.")