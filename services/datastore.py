import json
import os

class DataStore:
    FILE_PATH = "DATA/library.json"

    def load(self):
        if not os.path.exists(self.FILE_PATH):
            return {"users": [], "books": [], "loans": []}

        with open(self.FILE_PATH, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)