import sqlite3, cgitb
cgitb.enable()
from flask import g
dbFile = 'approot/appdata.db'

def get_db():
    connection = g.get('db','null')
    if connection == 'null':
        g.db = sqlite3.connect(dbFile)
        g.db.row_factory = sqlite3.Row
        return g.db
    else:
        return connection