


#include <Adafruit_FXOS8700.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>

/* Assign a unique ID to this sensor at the same time */
Adafruit_FXOS8700 accelmag = Adafruit_FXOS8700(0x8700A, 0x8700B);

void setup() {
  Serial.begin(9600);
  
  //Wait for serial monitor 
  while (!Serial){
    delay(1);
  }

  Serial.println("FXOS8700 Test");
  //initialize sensors 
  if (!accelmag.begin()) {
    Serial.println("No FXOS8700 detected. Check connections");
    while (1);
  }
  
}

void loop() {
  sensors_event_t AccelEvent, MagEvent;

  accelmag.getEvent(&AccelEvent,&MagEvent);
  
  Serial.print(MagEvent.magnetic.x, 6);
  Serial.print(",");
  Serial.print(MagEvent.magnetic.y, 6);
  Serial.print(",");
  Serial.println(MagEvent.magnetic.z, 6);

  delay(100);
  

  

}
