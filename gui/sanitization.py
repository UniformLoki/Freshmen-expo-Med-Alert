import datetime, re

def check_birthdate(birthdate:str|datetime.date) -> str:
    format = "%Y-%m-%d"
    current_time = datetime.datetime.now()
    if isinstance(birthdate, str):
        try:
            birthdate_obj = datetime.datetime.strptime(birthdate, format)
        except:
            birthdate_obj = current_time
    elif isinstance(birthdate, datetime.date):
        birthdate_obj = birthdate
    if birthdate_obj <= current_time:
        return birthdate_obj
    else:
        return current_time
    
def check_email(email:str) -> str|None:
    valid_email = re.search("@[a-zA-Z0-9.-]+[.]com|org|edu|cc", email)
    if valid_email:
        return email
    else:
        return None
    
def check_phone(phone:str) -> str|None:
    valid_phone = re.search("[2-9][0-9]{2}-[0-9]{3}-[0-9]{4}", phone)
    if valid_phone:
        return phone
    else:
        return None