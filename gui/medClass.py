import uuid

class Medication():

    def __init__(self, name:str, dose:str, schedule:list[str], amount:float, pill_weight:float) -> None:
        self.id = f"{uuid.uuid4()}"
        self.name = name
        self.dose = dose
        self.full_amount = amount
        self.current_amount = amount
        self.schedule = schedule
        self.pill_weight = pill_weight

    @property
    def name(self) -> str:
        # decryption stuff
        return self._name
    
    @name.setter
    def name(self, new_name:str) -> None:
        # encryption stuff
        self._name = new_name

    @property
    def dose(self) -> str:
        # decryption stuff
        return self._dose
    
    @dose.setter
    def dose(self, new_dose:str) -> None:
        # encryption stuff
        self._dose = new_dose

    @property
    def current_amount(self) -> float:
        return self._current_amount
    
    @current_amount.setter
    def current_amount(self, new_amount:float) -> None:
        if 0 <= new_amount <= self.full_amount:
            self._current_amount = new_amount