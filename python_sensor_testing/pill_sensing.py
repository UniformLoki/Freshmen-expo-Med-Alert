# Name: Rachel Dahl
# Date: April 19, 2024
# Description: File used to detect removal of pills
# from weight plate
# This code uses the HX711 library by gandalf15, found here:
# https://github.com/gandalf15/HX711


from constants import *

#set up GPIO
GPIO.setmode(GPIO.BCM)

#instantiate scale
scale = HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)

#calibrate
scale.set_scale_ratio(CALIBRATION_FACTOR)

#weigh one pill
input("Place one dose on the scale, then press enter to weigh it.")
single_dose_in_g = scale.get_weight_mean(5)
print(f"One dose weighs {single_dose_in_g} g")

#get initial mass
input("Place the bottle(s) on the scale, then press enter to start tracking.")
initial_mass = scale.get_weight_mean(5)

TRACKING = True

#track pill removal
while TRACKING:

    #get mass
    current_mass = scale.get_weight_mean(5)

    #find change in mass
    mass_difference = initial_mass - current_mass

    if mass_difference >= single_dose_in_g - TOLERANCE:
        doses_removed = mass_difference // single_dose_in_g
        print(f"{doses_removed} doses wore removed")

    initial_mass = current_mass
