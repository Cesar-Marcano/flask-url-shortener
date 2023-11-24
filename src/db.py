import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))

def conn():
    return sqlite3.connect(os.path.join(dir_path, "../database.db"))

def init():
    connection = conn()
    with open(os.path.join(dir_path, "./sql/schema.sql")) as f:
        connection.executescript(f.read())
    connection.close()

def create_url(title, url):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO urls (title, url) VALUES (?, ?)", (title, url))
    connection.commit()
    connection.close()

def read_url(id):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM urls WHERE id=?", (id,))
    result = cursor.fetchone()
    connection.close()
    return result

def update_url(id, title, url):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("UPDATE urls SET title=?, url=? WHERE id=?", (title, url, id))
    connection.commit()
    connection.close()

def delete_url(id):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM urls WHERE id=?", (id,))
    connection.commit()
    connection.close()
