import json
import os

FILE_PATH = "data/library_data.json"

class DataStore:

    @staticmethod
    def load():
        if not os.path.exists(FILE_PATH):
            return {"members": [], "books": [], "loans": []}

        with open(FILE_PATH, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):
        os.makedirs("data", exist_ok=True)
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)