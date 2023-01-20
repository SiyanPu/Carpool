import sqlite3

connection = sqlite3.connect('database.sqlite')


with open('database.sql') as f:
    query = f.read()
    connection.executescript(query)

connection.commit()
connection.close()