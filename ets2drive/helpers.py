import yaml
import json
import os


def read_yaml(config_path):
    """Load config files."""
    with open(config_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data

def read_json(fpath):
    with open(fpath) as f:
        data = json.load(f)
    return data