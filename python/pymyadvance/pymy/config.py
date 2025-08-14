import os
import yaml

with open("db.yaml", "r") as f:
    DB_CONFIG = yaml.safe_load(f)

SECRET_KEY = "mon926732@"