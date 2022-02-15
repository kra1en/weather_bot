import json
from types import SimpleNamespace


def parse_config(config_file_name):
    file = open(config_file_name, "r")
    config = json.loads(file.read(), object_hook=lambda data: SimpleNamespace(**data))
    file.close()
    return config
