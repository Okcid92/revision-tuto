import yaml
import os


BASE_DIR = os.path.dirname(__file__)  # dossier où est config.py
DB_PATH = os.path.join(BASE_DIR, "db.yaml")


with open(DB_PATH, 'r') as f:
    DB_CONFIG = yaml.safe_load(f)

SECRET_KEY = 'mon926732@'