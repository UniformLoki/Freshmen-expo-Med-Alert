import sqlite3, os
db = os.path.join('gui', 'appdata.db')
connection = sqlite3.connect(db)
sql = connection.cursor()

import tkinter as tk
from tkhtmlview import HTMLLabel

html = ""

def showData(data):
    global html

    names = list(map(lambda x: x[0], data.description))
    html += "<table><tbody>"

    html += "<tr>"
    for heading in names:
        html += f"<th>{heading}</th>"
    html += "</tr>"

    for row in data:
        html += "<tr>"
        for data in row:
            html += f"<td>{data}</td>"
        html += "</tr>"
    html += "</tbody></table>"

#### EDITABLE ####

from flask import Flask
from userdata import create_tables, add_profile

app = Flask(__name__)
with app.app_context():
    create_tables()
    
html += '<h3>Profiles:</h3>'
showData(sql.execute("select * from Profiles"))
html += '<br><hr><br>'
html += '<h3>Medications:</h3>'
showData(sql.execute('select * from Medications'))
html += '<br><hr><br>'

#### DISPLAY ####

root = tk.Tk()
root.geometry("900x600")

html_label = HTMLLabel(root, html=html)
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()