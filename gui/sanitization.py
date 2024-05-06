import datetime, re

def check_birthdate(birthdate:str) -> str:
    format = "%Y-%m-%d"
    current_time = datetime.datetime.now()
    birthdate_obj = datetime.datetime.strptime(birthdate, format)
    if birthdate_obj <= current_time:
        return birthdate
    else:
        return datetime.datetime.strftime(current_time, format)
    
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