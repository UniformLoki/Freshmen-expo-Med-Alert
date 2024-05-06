class Contact:

    def __init__(self, contact_id:int, profile_id:int, name:str, relation:str, email:str, phone:str) -> None:
        self.id = contact_id
        self.profile = profile_id
        self.name = name
        self.relation = relation
        self.email = email
        self.phone = phone