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
