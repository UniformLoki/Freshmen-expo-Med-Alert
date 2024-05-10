class Medication:

    def __init__(self, medID:int, profile, name:str, dose:str, full_amount:float, current_amount:float, pill_weight:float, low:bool) -> None:
        self.id = medID
        self.profile = profile
        self.name = name
        self.dose = dose
        self.full_amount = full_amount
        self.current_amount = current_amount
        self.pill_weight = pill_weight
        self.low = low