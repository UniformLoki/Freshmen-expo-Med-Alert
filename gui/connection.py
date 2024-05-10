import sqlite3, os
from flask import g
dbFile = os.path.join('gui', 'appdata.db')

def get_db():
    connection = g.get('db','null')
    if connection == 'null':
        g.db = sqlite3.connect(dbFile)
        g.db.row_factory = sqlite3.Row
        return g.db
    else:
        return connection