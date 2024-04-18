//declare constants
int FORCE_SENSOR = 4;

void setup() {

  //initialize serial

  Serial.begin(9600);
  Serial.println("Weight Sensor Testing\n");


  //check that sensor is actually returning values

  Serial.println("Check that the sensor is actually returning values\n");
  Serial.println("Try putting a small amount of force on the sensor and see how it responds\n");

  for(int i=0; i < 7; i++){
    int AnalogValue = analogRead(FORCE_SENSOR);
    Serial.print("AnalogValue = ");
    Serial.println(AnalogValue);
    delay(1500);
  }


  //get an initial value with nothing on the sensor

  Serial.println("\nGetting an initial value with nothing on the sensor\n");
  Serial.println("Please lay the sensor down flat and make sure nothing is touching it");
  Serial.println("Press any key to continue\n");

  while (Serial.available() == 0){ //pauses code until a key is pressed

  }
  Serial.read(); //clears whatever was entered in the monitor

  int InitialAnalogValue = analogRead(FORCE_SENSOR);
  Serial.print("Analog value with nothing on the sensor: ");
  Serial.println(InitialAnalogValue);


  delay(500);


  //see if sensor recognizes weight of a bottle
  //plastic cup substituted for initial testing

  Serial.println("\nSee if sensor recognizes weight of bottle\n");
  Serial.println("Place the cup on the sensor and then press any key.\n");

  while (Serial.available() == 0){

  }
  Serial.read();


  int AnalogValueWithBottle = analogRead(FORCE_SENSOR);

  if(AnalogValueWithBottle != InitialAnalogValue){
    Serial.println("Bottle detected");
  }

  Serial.println("Without bottle\tWith bottle");
  Serial.print(InitialAnalogValue);
  Serial.print("\t\t\t");
  Serial.print(AnalogValueWithBottle);


  delay(500);


  //see if sensor can detect the weight of 
  //a single pill
  //small candies substituted for initial testing 

  Serial.println("\nCheck if sensor can detect the weight of a single pill\n");
  Serial.println("Take the bottle off the sensor and place one pill on it");
  Serial.println("Press any key to continue\n");

  while (Serial.available() == 0){

  }
  Serial.read();


  int AnalogValOfOnePill = analogRead(FORCE_SENSOR);

  Serial.print("Analog value of one pill: ");
  Serial.println(AnalogValOfOnePill);


  delay(500);


  //see if sensor can recognize when a pill is
  //removed from the bottle

  Serial.println("\nSee if sensor can detect when a pill is removed\n");
  Serial.println("Put several pills in the bottle and place it on the sensor");
  Serial.println("Press any key to continue\n");

  while (Serial.available() == 0){ 

  }
  Serial.read();

  int AnalogValOfBottleWithPills = analogRead(FORCE_SENSOR);

  Serial.println("Now remove one pill from the bottle and press any key");

  while (Serial.available() == 0){

  }
  Serial.read();

  int AnalogValOfBottleWithOnePillTakenOut = analogRead(FORCE_SENSOR);

  if(AnalogValOfBottleWithPills != AnalogValOfBottleWithOnePillTakenOut){
    Serial.println("A pill was removed");
  }

  Serial.println("With all pills\tWith one pill removed");
  Serial.print(AnalogValOfBottleWithPills);
  Serial.print("\t\t\t");
  Serial.print(AnalogValOfBottleWithOnePillTakenOut);


}

void loop() {
  
}
