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
from userdata import *
# from encryption import encrypt, decrypt

app = Flask(__name__)
with app.app_context():
    create_tables()

    add_profile("Jason Thompson", "1969-03-15", "jason.thompson@example.com", '555-123-4567', False)
    add_profile("Sara Thompson", "1968-11-7", "sara.johnson@example.com", '555-987-6543', False)
    add_profile('Michael Johnson', '2004-02-22', 'michael.johnson@example.com', '555-234-5678', True, "Sara Johnson", "Parent/Guardian", 'sara.johnson@example.com', '555-987-6543')

    add_medication(1, "Omeprazole", "20mg", 100, 0.025, ['09:00'])
    add_medication(1, "Metformin", "500mg", 90, 0.05, ['09:00', '21:00'])
    add_medication(2, "Atorvastatin", "20mg", 90, 0.075, ['08:00'])
    add_medication(3, "Concerta", "25mg", 90, 0.025, ['08:00'])
    add_medication(3, "Olanzapine", "2.5mg", "8", 0.1, ['08:00', '12:00', '18:00'], True)

html += '<h3>Profiles:</h3>'
showData(sql.execute("select * from Profiles"))
html += '<br><hr><br>'
html += '<h3>Contacts:</h3>'
showData(sql.execute('select * from Contacts'))
html += '<br><hr><br>'
html += '<h3>Medications:</h3>'
showData(sql.execute('select * from Medications'))
html += '<br><hr><br>'
html += '<h3>Alarms:</h3>'
showData(sql.execute('select * from Alarms'))
html += '<br><hr><br>'

#### DISPLAY ####

root = tk.Tk()
root.geometry("900x600")

html_label = HTMLLabel(root, html=html)
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()