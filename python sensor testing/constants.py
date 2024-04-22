# Name: Rachel Dahl
# Date: April 19, 2024
# Description: Constants used in other files
# This code uses the HX711 library by gandalf15, found here:
# https://github.com/gandalf15/HX711



#libraries
import pineworkslabs.RPi as GPIO
from hx711 import HX711
from time import sleep


#pin numbers
DT_PIN = 0
SCK_PIN = 0


#calibration
CALIBRATION_FACTOR = 28510 #calculated in calibration.py file