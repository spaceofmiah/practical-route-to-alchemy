import configparser
import pathlib

# Setup base directory
BASE_PATH = pathlib.Path(".").absolute()

# Load environment variables
config = configparser.ConfigParser()
config.read(BASE_PATH.joinpath("config.ini"))

# get database configurations
DATABASE = {
    'USERNAME': config['database']['username'],
    'PASSWORD': config['database']['password'],
    'HOST': config['database']['host'],
    'PORT': config['database']['port'],
    'NAME': config['database']['name'],
}
