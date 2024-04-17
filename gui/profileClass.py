import uuid, datetime, re

class Profile:

    def __init__(self, name:str, birthdate:str, email:str=None, phone:str=None) -> None:
        self.id = f"{uuid.uuid4()}"
        self.name = name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.medications = []
        self.date_added = datetime.datetime.now().strftime("%m/%d/%Y")

    @property
    def birthdate(self) -> str:
        return self._birthdate
    
    @birthdate.setter
    def birthdate(self, new_birthdate:str) -> None:
        format = "%m/%d/%Y"
        new_birthdate_formatted = datetime.datetime.strptime(new_birthdate, format)
        current_time = datetime.datetime.now()
        if new_birthdate_formatted <= current_time:
            self._birthdate = new_birthdate
        else:
            self._birthdate = current_time.strftime(format)

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, new_email:str) -> None:
        valid_email = re.search("@[a-zA-Z0-9.-]+[.]com|org|edu|cc", new_email)
        if valid_email:
            self._email = new_email
    
    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, new_phone:str) -> None:
        valid_phone = re.search("\([2-9][0-9]{2}\)-[0-9]{3}-[0-9]{4}", new_phone)
        if valid_phone:
            self._phone = new_phone