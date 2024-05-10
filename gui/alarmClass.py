from datetime import datetime

class Alarm:

    def __init__(self, alarmID:int, med, time:str) -> None:
        self.id = alarmID
        self.med = med
        self.time_obj = time
        self.time_str = datetime.strftime(time, "%I:%M %p")