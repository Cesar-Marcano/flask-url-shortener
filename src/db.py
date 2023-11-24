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


def create_url(title, url, slug):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO urls (title, url_path, slug) VALUES (?, ?, ?)", (title, url, slug))
    connection.commit()
    connection.close()


def read_url(slug):
    connection = conn()
    cursor = connection.cursor()
    cursor.execute("SELECT (url_path) FROM urls WHERE slug=?", (slug,))
    result = cursor.fetchone()
    connection.close()
    return result
