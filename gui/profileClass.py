class Profile:

    def __init__(self, profileID:int, added:str, name:str, birthdate:str, email:str=None, phone:str=None) -> None:
        self.id = profileID
        self.date_added = added
        self.name = name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone