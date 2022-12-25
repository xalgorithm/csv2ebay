import yaml

def read_config():
    with open('config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg
