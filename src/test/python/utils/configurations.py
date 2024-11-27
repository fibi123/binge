import os
import json

USER_DATA_PATH = "A:/Binge/src/test/resources/testdata/user_data.json"

def get_user_data(key):
    if not os.path.exists(USER_DATA_PATH):
        raise FileNotFoundError(f"File not found: {USER_DATA_PATH}")
    with open(USER_DATA_PATH, "r") as file:
        data = json.load(file)
        return data.get(key)

#def window_transition():
