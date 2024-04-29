class Medication:

    def __init__(self, medID:int, profile:int, name:str, dose:str, full_amount:float, current_amount:float, schedule:list[str], pill_weight:float) -> None:
        self.id = medID
        self.profileID = profile
        self.name = name
        self.dose = dose
        self.full_amount = full_amount
        self.current_amount = current_amount
        self.schedule = schedule
        self.pill_weight = pill_weight