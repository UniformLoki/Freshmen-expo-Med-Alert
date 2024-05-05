from datetime import datetime

class Alarm:

    def __init__(self, alarm_id:int, med, time:str) -> None:
        self.id = alarm_id
        self.med = med
        self.time_obj = time
        self.time_str = datetime.strftime(time, "%I:%M %p")