import sqlite3
from config import Config

def connect():
    return sqlite3.connect(Config.DB_NAME)
