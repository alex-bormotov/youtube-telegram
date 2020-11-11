import json


def get_config(config_file):
    with open(config_file, "r") as read_file:
        return json.load(read_file)
