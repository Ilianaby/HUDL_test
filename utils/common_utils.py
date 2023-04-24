from os import path
import yaml

def read_config(*args):
    values = []
    path_file = path.dirname(__file__) + '/../config.yml'
    with open(path_file, 'r') as f:
        config = yaml.safe_load(f)
    for arg in args:
        values.append(config[arg])
    return values

