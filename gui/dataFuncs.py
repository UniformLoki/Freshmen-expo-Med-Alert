from medClass import *
from meds import *
from profileClass import *
from profiles import *

def add_profile(name:str, birthdate:str, email:str=None, phone:str=None) -> None:
    new_profile = Profile(name, birthdate, email, phone) # instantiate new profile
    profiles[new_profile.id] = new_profile # add it to profile database

def del_profile(profile:Profile) -> None:
    profiles.pop(profile.id)

def add_medication(profile:Profile, name:str, dose:str, schedule:list[str], amount:float, pill_weight:float) -> None:
    new_medication = Medication(name, dose, schedule, amount, pill_weight) # instantiate new medication
    meds[new_medication.id] = new_medication # add it to medication database
    profiles[profile.id].medications.append(new_medication) # add medication to profile data

def del_medication(profile:Profile, medication:Medication) -> None:
    meds.pop(medication.id) # remove medication from meds database
    profile_meds = profiles[profile.id].medications
    for med in profile_meds:
        if med.id == medication.id:
            profile_meds.remove(medication) # remove medication from profile data

### note: look into pickle module to write data permanently to dictionaries.
