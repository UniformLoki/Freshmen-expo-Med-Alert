//code to detect when a pill is removed from the bottle
//uses some code from Nathan Seidle's SparkFun_HX711_Example.ino program

#include "HX711.h" 

#define CALIBRATION_FACTOR  28510.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2

float SinglePill = 0;
float StartingMass = 0;
float PRECISION = 0.005; //mass changes will be recognized if they are within +/- this number from the target

HX711 scale;


void setup() {
  //initialize serial
  Serial.begin(9600);

  //set up scale
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(CALIBRATION_FACTOR);
  scale.tare();

  Serial.println("Place a single pill on the scale, then press enter.");
  Serial.println("This calibrates the scale so it can recognize how many pills were removed.");

  while (Serial.available() == 0){} //pauses code until a key is pressed
  Serial.parseInt(); //clear serial monitor

  //get mass of single pill
  SinglePill = scale.get_units();
  Serial.print("One pill weighs ");
  Serial.print(SinglePill, 3);
  Serial.print(" kg"); 
  Serial.println();

  Serial.println("Place the bottle of pills on the scale.");
  Serial.println("Press enter to start tracking pills");

  while (Serial.available() == 0){} //pauses code until a key is pressed
  Serial.parseInt(); //clear serial monitor

  //get initial mass of bottle and pills
  StartingMass = scale.get_units();

  Serial.println("Pill tracking started");

  Serial.print("The bottle currently contains ");
  Serial.print(ceil(StartingMass / SinglePill), 0);
  Serial.println(" pills");

}

void loop() {
 
  //get current mass on scale
  float CurrentMass = scale.get_units();

  //find difference in mass
  float MassDifference = StartingMass - CurrentMass;

  //check for pill removal
  if (MassDifference >= SinglePill - PRECISION){

    int NumPillsTaken = ceil(MassDifference / SinglePill);
    Serial.print(NumPillsTaken);
    Serial.println("pill(s) were removed");
    StartingMass = CurrentMass;

  }

  //delay 2s between removal checks
  delay(2000);

}

