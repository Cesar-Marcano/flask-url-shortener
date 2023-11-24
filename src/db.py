import os
import sqlite3


dir_path = os.path.dirname(os.path.realpath(__file__))


def conn():
    return sqlite3.connect(os.path.join(dir_path, '../database.db'))


def init():
    connection = conn()
    

    with open(os.path.join(dir_path, './sql/schema.sql')) as f:
        connection.executescript(f.read())
    
    connection.close()
