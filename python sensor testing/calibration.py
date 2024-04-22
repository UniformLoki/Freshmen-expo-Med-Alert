# Name: Rachel Dahl
# Date: April 19, 2024
# Description: Generates a calibration factor to 
# adjust raw data from the sensor. After running this code,
# change the CALIBRATION_FACTOR in the constants.py file 
# to the value calculated here
# This code uses the HX711 library by gandalf15, found here:
# https://github.com/gandalf15/HX711

from constants import *


GPIO.setmode(GPIO.BCM)                 # set GPIO pin mode to BCM numbering
scale = HX711()

