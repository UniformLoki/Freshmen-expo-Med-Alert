class Profile:

    def __init__(self, profileID:int, added:str, name:str, birthdate:str, email:str, phone:str, paired:bool, contactID:int|None=None) -> None:
        self.id = profileID
        self.date_added = added
        self.name = name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.paired = paired
        self.contact = contactID