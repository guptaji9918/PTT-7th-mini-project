import json
import os

def import_records(input_path):
    if os.path.exists(input_path):
        with open(input_path, "r", encoding="utf-8") as file:
            return json.load(file)
    with open(input_path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_outputs(accepted, rejected, valid_path, error_path):
    with open(valid_path, "w", encoding="utf-8") as file:
        json.dump(accepted, file, indent=4)

    with open(error_path, "w", encoding="utf-8") as file:
        if rejected:
            file.writelines(message + "\n" for message in rejected)
        else:
            file.write("No rejected records.\n")