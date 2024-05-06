from constants import *

#try:
GPIO.setmode(GPIO.BCM)
scale = HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)
error = scale.zero( )
if error:
    raise ValueError("Tare unsuccessful")
    
reading = scale.get_raw_data_mean()
if reading:
    print("raw, unitless data subtracted from offset: ", reading)
else:
    print("invalid data")
        
input("place a known weight on the scale, then press enter.")
reading = scale.get_data_mean()
if reading:
    known_weight_grams = input("type the known weight in grams, then press enter")
    try:
        value = float(known_weight_grams)
        print(value, "grams")
    except ValueError:
        print("must be integer or float")
            
    ratio = reading / value
    scale.set_scale_ratio(ratio)
    print("calibration factor is ", ratio)
        
else:
    raise ValueError("Cannot calculate mean value.")

#except:
    #print("something went wrong.")
