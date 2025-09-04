import sqlite3
def connect():
    con = sqlite3.connect("hamburgueseria.db")
    return con