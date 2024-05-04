from connection import get_db
from sanitization import *
from profileClass import Profile
from medClass import Medication
# from encryption import encrypt, decrypt
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
    
    sql.execute('''CREATE TABLE IF NOT EXISTS Schedules (
                "medID" integer primary key autoincrement,
                "time_1" text,
                "time_2" text,
                "time_3" text,
                "time_4" text,
                "time_5" text,
                "time_6" text,
                "time_7" text,
                "time_8" text,
                "time_9" text,
                "time_10" text,
                "time_11" text,
                "time_12" text,
                "time_13" text,
                "time_14" text,
                "time_15" text,
                "time_16" text,
                "time_17" text,
                "time_18" text,
                "time_19" text,
                "time_20" text,
                "time_21" text,
                "time_22" text,
                "time_23" text,
                "time_24" text
                )''')
    

# PROFILES

def add_profile(name:str, birthdate:str, email:str, phone:str, paired:bool, contact_name:str|None=None, contact_relation:str|None=None, contact_email:str|None=None, contact_phone:str|None=None) -> None:
    con = get_db()
    sql = con.cursor()

    added = datetime.datetime.now().strftime("%Y-%m-%d")

    # sanitization
    sanit_birthdate = check_birthdate(birthdate)
    sanit_email = check_email(email)
    sanit_phone = check_phone(phone)

    sql.execute('INSERT INTO Profiles (Added, Name, Birthdate, Email, Phone, Paired) VALUES (?, ?, ?, ?, ?, ?)', [added, name, sanit_birthdate, sanit_email, sanit_phone, paired])

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
    return Profile(*profile_data)

def update_name(profile_id:int, name:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Profiles SET Name='{name}' WHERE profileID={profile_id}")
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
        # get contactID
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
        sql.execute(f'DELETE FROM Schedules WHERE medID={del_id[0]}')
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

def update_contact_name(contact_id:int, name:str) -> None:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"UPDATE Contacts SET Name='{name}' WHERE contactID={contact_id}")
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
    sql.execute('INSERT INTO Schedules (time_1) VALUES (NULL)')

    # get id
    sql.execute('SELECT medID FROM Medications ORDER BY medID DESC LIMIT 1')
    med_id = sql.fetchone()[0]

    # log schedule
    time_slot = 1
    for i in range(24): # for all the possible time slots,
        if i < len(schedule): # if that time slot is used,
            # insert value
            sql.execute(f'UPDATE Schedules SET time_{time_slot}="{schedule[i]}" WHERE medID={med_id}')
        else: # if not,
            # insert NULL
            sql.execute(f'UPDATE Schedules SET time_{time_slot}=NULL WHERE medID={med_id}')
        time_slot += 1 # next slot
    con.commit()

def get_medication(med_id:int) -> Medication:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Medications WHERE medID={med_id}")
    med_data = sql.fetchone()
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

def get_schedule(med_id:int) -> list[datetime.time]:
    con = get_db()
    sql = con.cursor()
    sql.execute(f"SELECT * FROM Schedules WHERE medID={med_id}")
    schedule_list = list(sql.fetchone())
    return list(filter(lambda x: x != None, schedule_list))

def update_dose(med_id:int, dose:str) -> None:
    con = get_db()
    sql = con.cursor()
    crypt_dose = encrypt(dose)
    sql.execute(f"UPDATE Medications SET Dose='{crypt_dose}' WHERE medID={med_id}")
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
    for i in range(1, 25):
        sql.execute(f"UPDATE Schedules SET time_{i}=NULL WHERE medID={med_id}")
    
    # insert new one
    time_slot = 1
    for i in range(24): # for all the possible time slots,
        if i < len(schedule): # if that time slot is used,
            # insert value
            sql.execute(f'UPDATE Schedules SET time_{time_slot}="{schedule[i]}" WHERE medID={med_id}')
        else: # if not,
            # insert NULL
            sql.execute(f"UPDATE Schedules SET time_{time_slot}=NULL WHERE medID={med_id}")
        time_slot += 1 # next slot
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
    sql.execute(f'DELETE FROM Schedules WHERE medID={med_id}')
    con.commit()


# ALARMS

def get_next_alarm() -> str:
    con = get_db()
    sql = con.cursor()