//code to detect when a pill is removed from the bottle
//uses some code from Nathan Seidle's SparkFun_HX711_Example.ino program

#include "HX711.h" 

#define calibration_factor  28510.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2

float single_pill = 0

HX711 scale;


void setup() {
  //initialize serial
  Serial.begin(9600);

  //set up scale
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor);
  scale.tare();

  serial.println("Place a single pill on the scale, then press enter.");
  serial.println("this calibrates the scale so it can recognize how many pills were removed.");

  while (Serial.available() == 0){} //pauses code until a key is pressed

  single_pill = scale.get_units();
  Serial.print("One pill weighs ");
  Serial.print(single_pill, 3);
  Serial.print(" kg"); 
  Serial.println();

  serial.println("Place the bottle of pills on the scale.")
  serial.println("Press enter to start tracking pills")

  while (Serial.available() == 0){} //pauses code until a key is pressed

}

void loop() {
  

}

