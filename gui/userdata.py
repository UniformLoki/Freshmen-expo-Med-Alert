from connection import get_db
from sanitization import *
from profileClass import Profile
from medClass import Medication
import datetime

# TABLES

def create_tables():
    con = get_db()
    sql = con.cursor()
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Profiles (
                "profileID" integer primary key autoincrement,
                "Added" date,
                "Name" text,
                "Birthdate" date,
                "Email" text,
                "Phone" text
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
    

# PROFILES

def add_profile(name:str, birthdate:str, email:str=None, phone:str=None) -> None:
    con = get_db()
    sql = con.cursor()

    added = datetime.datetime.now().strftime("%Y-%m-%d")

    # sanitization
    sanit_birthdate = check_birthdate(birthdate)
    sanit_email = check_email(email)
    sanit_phone = check_phone(phone)

    sql.execute('INSERT INTO Profiles (Added, Name, Birthdate, Email, Phone) VALUES (?, ?, ?, ?, ?)', [added, name, sanit_birthdate, sanit_email, sanit_phone])
    con.commit()

def get_profile(profile:int) -> Profile:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Profiles WHERE profileID={profile}")
    profile_data = sql.fetchone()
    return Profile(*profile_data)

def update_name(profile:int, name:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Profiles SET Name='{name}' WHERE profileID={profile}")
    con.commit()

def update_email(profile:int, email:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_email = check_email(email)
    if sanit_email != None:
        sql.execute(f"UPDATE Profiles SET Email='{sanit_email}' WHERE profileID={profile}")
    con.commit()

def update_phone(profile:int, phone:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_phone = check_phone(phone)
    if sanit_phone != None:
        sql.execute(f"UPDATE Profiles SET Phone='{sanit_phone}' WHERE profileID={profile}")
    con.commit()

def del_profile(profile:int) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f'DELETE FROM Profiles WHERE profileID={profile}')
    con.commit()


# MEDICATIONS

def add_medication(profile:int, name:str, dose:str, amount:float, schedule:list[str], pill_weight:float) -> None:
    con = get_db()
    sql = con.cursor()

    sql.execute('INSERT INTO Medications (profileID, Name, Dose, Full_Amount, Current_Amount, Schedule, Pill_Weight) VALUES (?, ?, ?, ?, ?, ?, ?)', [profile, name, dose, amount, amount, schedule, pill_weight])
    con.commit()

def get_medication(med:int) -> Medication:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Medications WHERE medID={med}")
    med_data = sql.fetchone()
    return Medication(*med_data)

def update_dose(profile:int, dose:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Dose='{dose}' WHERE profileID={profile}")
    con.commit()

def update_full_amount(profile:int, full_amount:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Full_Amount='{full_amount}' WHERE profileID={profile}")
    con.commit()

def update_current_amount(profile:int, current_amount:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Current_Amount='{current_amount}' WHERE profileID={profile}")
    con.commit()

def update_schedule(profile:int, schedule:list) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Schedule='{schedule}' WHERE profileID={profile}")
    con.commit()

def update_pill_weight(profile:int, pill_weight:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Pill_Weight='{pill_weight}' WHERE profileID={profile}")
    con.commit()

def del_medication(med:int) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f'DELETE FROM Medications WHERE medID={med}')
    con.commit()