from connection import get_db
from sanitization import *
from profileClass import Profile
from medClass import Medication
from alarmClass import Alarm
from contactClass import Contact
# from encryption import encrypt, decrypt
from datetime import datetime

# TABLES

def create_tables():
    con = get_db()
    sql = con.cursor()
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Profiles (
                "profileID" integer primary key autoincrement,
                "Name" text,
                "Birthdate" text,
                "Email" text,
                "Phone" text,
                "Paired" bool,
                "contactID" int,
                foreign key (contactID) references Contacts(contactID)
                )''')
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Contacts (
                "contactID" integer primary key autoincrement,
                "profileID" integer,
                "Name" text,
                "Relation" text,
                "Email" text,
                "Phone" text,
                foreign key (profileID) references Profiles(profileID)
                )''')
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Medications (
                "medID" integer primary key autoincrement,
                "profileID" integer,
                "Name" text,
                "Dose" text,
                "Full_Amount" float,
                "Current_Amount" float,
                "Pill_Weight" float,
                "Low" bool,
                foreign key (profileID) references Profiles(profileID)
                )''')
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Alarms (
                "alarmID" integer primary key autoincrement,
                "medID" integer,
                "Time" text,
                foreign key (medID) references Medications(medID)
                )''')
    

# PROFILES

def add_profile(name:str, birthdate:str, email:str, phone:str, paired:bool, contact_name:str|None=None, contact_relation:str|None=None, contact_email:str|None=None, contact_phone:str|None=None) -> None:
    con = get_db()
    sql = con.cursor()

    # sanitization
    sanit_birthdate = check_birthdate(birthdate)
    sanit_email = check_email(email)
    sanit_phone = check_phone(phone)

    sql.execute('INSERT INTO Profiles (Name, Birthdate, Email, Phone, Paired) VALUES (?, ?, ?, ?, ?)', [name, sanit_birthdate, sanit_email, sanit_phone, paired])

    if paired:
        # get id
        sql.execute('SELECT profileID FROM Profiles ORDER BY profileID DESC LIMIT 1')
        profile_id = sql.fetchone()[0]
        # add contact
        add_contact(profile_id, contact_name, contact_relation, contact_email, contact_phone)

        # get contactID
        sql.execute('SELECT contactID FROM Contacts ORDER BY contactID DESC LIMIT 1')
        contact_id = sql.fetchone()[0]
        # add contact to profile
        sql.execute(f'UPDATE Profiles SET contactID={contact_id} WHERE profileID={profile_id}')

    con.commit()

def get_profile(profile_id:int) -> Profile:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Profiles WHERE profileID={profile_id}")
    profile_data = sql.fetchone()
    profile = Profile(*profile_data)
    if profile.contact != None:
        profile.contact = get_contact(profile.contact)
    return profile

def get_profiles() -> list[Profile]:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Profiles ORDER BY Name")
    profile_data = [list(row) for row in list(sql.fetchall())]
    for profile in profile_data:
        profile[2] = datetime.strptime(profile[2], "%Y-%m-%d")
        profile[2] = datetime.strftime(profile[2], "%m/%d/%Y")
    return [Profile(*profile) for profile in profile_data]

def update_name(profile_id:int, name:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Profiles SET Name='{name}' WHERE profileID={profile_id}")
    con.commit()

def update_birthdate(profile_id:int, birthdate:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_birthdate = check_birthdate(birthdate)
    sql.execute(f"UPDATE Profiles SET Birthdate='{sanit_birthdate}' WHERE profileID={profile_id}")
    con.commit()

def update_email(profile_id:int, email:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_email = check_email(email)
    if sanit_email != None:
        sql.execute(f"UPDATE Profiles SET Email='{sanit_email}' WHERE profileID={profile_id}")
    con.commit()

def update_phone(profile_id:int, phone:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_phone = check_phone(phone)
    if sanit_phone != None:
        sql.execute(f"UPDATE Profiles SET Phone='{sanit_phone}' WHERE profileID={profile_id}")
    con.commit()

def update_paired(profile_id:int, paired:bool, contact_name:str|None=None, contact_relation:str|None=None, contact_email:str|None=None, contact_phone:str|None=None) -> None:
    con = get_db()
    sql = con.cursor()
    old_profile = get_profile(profile_id)

    sql.execute(f"UPDATE Profiles SET Paired={paired} WHERE profileID={profile_id}")

    if paired:
        # add contact
        add_contact(profile_id, contact_name, contact_relation, contact_email, contact_phone)

        # get contactID
        sql.execute('SELECT contactID FROM Contacts ORDER BY contactID DESC LIMIT 1')
        contact_id = sql.fetchone()[0]
        # add contact to profile
        sql.execute(f'UPDATE Profiles SET contactID={contact_id} WHERE profileID={profile_id}')
    else:
        # if has contact, get contactID and delete
        if old_profile.contact != 0:
            sql.execute(f'UPDATE Profiles SET contactID=NULL WHERE profileID={profile_id}')
            sql.execute(f'SELECT contactID FROM Contacts WHERE profileID={profile_id}')
            contact_id = sql.fetchone()[0]
            del_contact(contact_id)
    con.commit()

def del_profile(profile_id:int) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT medID FROM Medications WHERE profileID={profile_id}")
    del_ids = [tuple(x) for x in sql.fetchall()]
    for del_id in del_ids:
        sql.execute(f'DELETE FROM Alarms WHERE medID={del_id[0]}')
    sql.execute(f'DELETE FROM Profiles WHERE profileID={profile_id}')
    sql.execute(f"DELETE FROM Medications WHERE profileID={profile_id}")
    sql.execute(f'DELETE FROM Contacts WHERE profileID={profile_id}')
    con.commit()


# EMERGENCY CONTACTS

def add_contact(profile_id:int, name:str, relation:str, email:str, phone:str) -> None:
    con = get_db()
    sql = con.cursor()

    # sanitzation
    sanit_email = check_email(email)
    sanit_phone = check_phone(phone)

    sql.execute('INSERT INTO Contacts (profileID, Name, Relation, Email, Phone) VALUES (?, ?, ?, ?, ?)', [profile_id, name, relation, sanit_email, sanit_phone])
    con.commit()

def get_contact(contact_id:int) -> Contact:
    con = get_db()
    sql = con.cursor()
    sql.execute(f'SELECT * FROM Contacts WHERE contactID={contact_id}')
    return Contact(*sql.fetchone())

def update_contact_name(contact_id:int, name:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Contacts SET Name='{name}' WHERE contactID={contact_id}")
    con.commit()

def update_contact_relation(contact_id:int, relation:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Contacts SET Relation='{relation}' WHERE contactID={contact_id}")
    con.commit()

def update_contact_email(contact_id:int, email:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_email = check_email(email)
    if sanit_email != None:
        sql.execute(f"UPDATE Contacts SET Email='{sanit_email}' WHERE contactID={contact_id}")
    con.commit()

def update_contact_phone(contact_id:int, phone:str) -> None:
    con = get_db()
    sql = con.cursor()
    sanit_phone = check_phone(phone)
    if sanit_phone != None:
        sql.execute(f"UPDATE Contacts SET Phone='{sanit_phone}' WHERE contactID={contact_id}")
    con.commit()

def del_contact(contact_id:int) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"DELETE FROM Contacts WHERE contactID={contact_id}")
    con.commit()


# MEDICATIONS

def add_medication(profile_id:int, name:str, dose:str, amount:float, pill_weight:float, schedule:list[str], low:bool=False) -> None:
    con = get_db()
    sql = con.cursor()

    # encrypt
    # crypt_name = encrypt(name)
    # crypt_dose = encrypt(dose)

    # log medication
    sql.execute('INSERT INTO Medications (profileID, Name, Dose, Full_Amount, Current_Amount, Pill_Weight, Low) VALUES (?, ?, ?, ?, ?, ?, ?)', [profile_id, name, dose, amount, amount, pill_weight, low])

    # get id
    sql.execute('SELECT medID FROM Medications ORDER BY medID DESC LIMIT 1')
    med_id = sql.fetchone()[0]

    # log schedule
    for time in schedule:
        sql.execute(f"INSERT INTO Alarms (medID, Time) VALUES (?,?)", [med_id, time])
    con.commit()

def get_medication(med_id:int) -> Medication:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Medications WHERE medID={med_id}")
    med_data = [x for x in list(sql.fetchone())]

    profile_id = med_data[1]
    profile = get_profile(profile_id)

    med_data[1] = profile
    return Medication(*med_data)
    # med_obj = Medication(*med_data)

    # # decrypt
    # med_obj.name = decrypt(med_obj.name)
    # med_obj.dose = decrypt(med_obj.dose)

    # return med_obj

def get_medications_from_profile(profile_id:int) -> list[Medication]:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Medications WHERE profileID={profile_id}")
    med_list = sql.fetchall()
    return [Medication(*entry) for entry in med_list]
    # med_objs = [Medication(*entry) for entry in med_list]

    # # decrypt
    # for obj in med_objs:
    #     obj.name = decrypt(obj.name)
    #     obj.dose = decrypt(obj.dose)

    # return med_objs

def get_schedule(med_id:int) -> list[str]:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Alarms WHERE medID={med_id}")
    schedule_list = list(sql.fetchall())
    return [list(alarm)[2] for alarm in schedule_list]

def update_dose(med_id:int, dose:str) -> None:
    con = get_db()
    sql = con.cursor()
    # crypt_dose = encrypt(dose)
    sql.execute(f"UPDATE Medications SET Dose='{dose}' WHERE medID={med_id}")
    con.commit()

def update_full_amount(med_id:int, full_amount:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Full_Amount='{full_amount}' WHERE medID={med_id}")
    con.commit()

def update_current_amount(med_id:int, current_amount:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Current_Amount='{current_amount}' WHERE medID={med_id}")
    if current_amount <= 10:
        sql.execute(f"UPDATE Medications SET Low=TRUE WHERE medID={med_id}")
    else:
        sql.execute(f"UPDATE Medications SET Low=FALSE WHERE medID={med_id}")
    con.commit()

def update_schedule(med_id:int, schedule:list[str]) -> None:
    con = get_db()
    sql = con.cursor()
    # clear existing schedule
    sql.execute(f'DELETE FROM Alarms WHERE medID={med_id}')
    # insert new one
    for time in schedule:
        sql.execute(f"INSERT INTO Alarms (medID, Time) VALUES (?,?)", [med_id, time])
    con.commit()

def update_pill_weight(med_id:int, pill_weight:float) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Medications SET Pill_Weight={pill_weight} WHERE medID={med_id}")
    con.commit()

def del_medication(med_id:int) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f'DELETE FROM Medications WHERE medID={med_id}')
    sql.execute(f'DELETE FROM Alarms WHERE medID={med_id}')
    con.commit()

def get_low() -> list[Medication]|None:
    con = get_db()
    sql = con.cursor()
    sql.execute('SELECT medID FROM Medications WHERE Low=True')
    low_ids = [[*row] for row in list(sql.fetchall())]
    if len(low_ids) > 0:
        return [get_medication(low_id[0]) for low_id in low_ids]
    return None


# ALARMS

def get_next_alarm() -> str:
    con = get_db()
    sql = con.cursor()

    # get current time
    now = datetime.now()

    # get alarms as a list of datetime objs
    sql.execute('SELECT Time FROM Alarms')
    compare_list = [datetime.strptime(list(alarm)[0], "%I:%M %p") for alarm in list(sql.fetchall())]
    compare_list.sort()
    
    # compare which ones are upcoming,
    # and return the first that's equal to/after the current time
    for alarm in compare_list:
        if now.hour < alarm.hour or (now.hour == alarm.hour and now.minute <= alarm.minute):
            return datetime.strftime(alarm, "%I:%M %p")
        
def get_alarms() -> list[Alarm]:
    con = get_db()
    sql = con.cursor()

    sql.execute('SELECT * FROM Alarms')
    alarm_list = [list(alarm) for alarm in list(sql.fetchall())]

    for alarm in alarm_list:
        alarm[2] = datetime.strptime(alarm[2], "%I:%M %p")
        med_id = alarm[1]
        medication = get_medication(med_id)
        alarm[1] = medication

    alarm_list.sort(key=lambda alarm: alarm[2])  
    return [Alarm(*alarm) for alarm in alarm_list]