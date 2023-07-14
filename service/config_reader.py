import configparser


def read(file):
    config = configparser.ConfigParser()
    config.read(file)
    return config