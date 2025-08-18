from flask import Flask
import config
import mysql.connector

dbc = Flask(__name__)
dbc.config.from_object(config)

def connectdb():
    return mysql.connector.connect(
        host = config.DB_CONFIG['host'],
        user = config.DB_CONFIG['user'],
        password = config.DB_CONFIG['password'],
        database = config.DB_CONFIG['database']
    )