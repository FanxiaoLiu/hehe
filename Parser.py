import os
import json

class Parser:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "prereqs.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.prereqs = []

        ##Opens JSON file, initializes and saves it as a JSON object
        
        with open(abs_file_path, "r") as f:
            self.prereqs = json.load(f)