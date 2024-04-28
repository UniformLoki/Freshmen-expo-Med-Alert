from connection import get_db
from sanitization import *
import datetime

def create_tables():
    con = get_db()
    sql = con.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS Profiles (
                "profileID" integer primary key autoincrement,
                "Name" text,
                "Birthdate" date,
                "Email" text,
                "Phone" text,
                "Added" date
    )''')
    sql.execute('''CREATE TABLE IF NOT EXISTS Medications (
                "medID" integer primary key autoincrement,
                "profileID" integer,
                "Name" text,
                "Dose" text,
                "Full_Amount" float,
                "Current_Amount" float,
                "Schedule" list,
                "Pill_Weight" float,
                foreign key (profileID) references Profiles(profileID)
    )''')

def add_profile(name:str, birthdate:str, email:str=None, phone:str=None) -> None:
    con = get_db()
    sql = con.cursor()

    added = datetime.datetime.now().strftime("%Y-%m-%d")

    # sanitization
    sanit_birthdate = check_birthdate(birthdate)
    sanit_email = check_email(email)
    sanit_phone = check_phone(phone)

    sql.execute('insert into Profiles (Name, Birthdate, Email, Phone, Added) values (?, ?, ?, ?, ?)', [name, sanit_birthdate, sanit_email, sanit_phone, added])
    con.commit()