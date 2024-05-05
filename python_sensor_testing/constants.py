# Name: Rachel Dahl
# Date: April 19, 2024
# Description: Constants used in other files
# This code uses the hx711py library by j-dohnalek, found here:
# https://github.com/j-dohnalek/hx711py/tree/master



#libraries
import pineworkslabs.RPi as GPIO
from hx711 import HX711
from time import sleep


#pin numbers
DT_PIN = 23
SCK_PIN = 24


#calibration
#calculated in calibration.py file
OFFSET = 8418085.6875
RATIO = 261.5

#range in which weight changes are recognized (g)
TOLERANCE = 0.1