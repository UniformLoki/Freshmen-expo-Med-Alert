//code to detect when a pill is removed from the bottle
//uses some code from Nathan Seidle's SparkFun_HX711_Example.ino program

#include "HX711.h" 

#define calibration_factor  28510.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2

HX711 scale;


void setup() {
  //initialize serial
  Serial.begin(9600);

  //set up scale
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor;)
  scale.tare();

  serial.println("Place a single pill on the scale, then press enter.")
  serial.println("this calibrates the scale so it can recognize how many pills were removed.")
  
}

void loop() {
  

}

}

void loop() {
  

}