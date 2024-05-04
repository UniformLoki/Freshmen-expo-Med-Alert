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
from encryption import encrypt, decrypt

app = Flask(__name__)
with app.app_context():
    create_tables()

    add_profile("Elia Browning", "2005-09-03", "elia.browning205@gmail.com", '601-218-9723', True, "Amy Browning", "Mother", "inhiscare68@gmail.com", "601-218-4925")
    add_profile("Tristan Fulghum", "2004-04-10", "tlf@dummymail.com", "504-290-7703", False)

    add_medication(1, "Topiramate", "25mg", 90, 0.005, ["11:30 PM"])
    add_medication(1, "Concerta", "27mg", 30, 0.025, ["7:00 AM"])
    add_medication(1, "Calcium Gummy", "500mg", 100, 0.5, ["11:30 PM"])
    add_medication(2, "Antibiotic", "150mg", 15, 0.025, ["9:30 AM", "9:30 PM"])
    add_medication(2, "Allergy Meds", "1,000mg", 200, 0.025, ["9:30 AM", "9:30 PM"])

html += '<h3>Profiles:</h3>'
showData(sql.execute("select * from Profiles"))
html += '<br><hr><br>'
html += '<h3>Contacts:</h3>'
showData(sql.execute('select * from Contacts'))
html += '<br><hr><br>'
html += '<h3>Medications:</h3>'
showData(sql.execute('select * from Medications'))
html += '<br><hr><br>'
html += '<h3>Schedules:</h3>'
showData(sql.execute('select * from Schedules'))
html += '<br><hr><br>'

#### DISPLAY ####

root = tk.Tk()
root.geometry("900x600")

html_label = HTMLLabel(root, html=html)
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()