#include <Wire.h>
#include <Adafruit_FXOS8700.h>
#include <Adafruit_Sensor.h>

const int HANDSHAKE = 0;
const int STREAM = 1;

//time between data acquisition 
int daqDelay = 100; //100ms 10hz
int inByte;
/* Assign a unique ID to this sensor at the same time */
Adafruit_FXOS8700 accelmag = Adafruit_FXOS8700(0x8700A, 0x8700B);

void printMag() 
{
  // Using arduino sensor libraries to get accel and mag readings
  sensors_event_t AccelEvent, MagEvent;
  accelmag.getEvent(&AccelEvent,&MagEvent);
  // Write the results in serial port 
  if (Serial.availableForWrite())
  {
    Serial.print(MagEvent.magnetic.x, 6);
    Serial.print(",");
    Serial.print(MagEvent.magnetic.y, 6);
    Serial.print(",");
    Serial.println(MagEvent.magnetic.z, 6);
  }
}

void setup() {
  Serial.begin(115200);
  
  //Wait for serial monitor 
  while (!Serial)
  {
    delay(1);
  }
  
  //initialize sensors 
  Serial.println("FXOS8700 Test");
  if (!accelmag.begin()) 
  {
    Serial.println("No FXOS8700 detected. Check connections");
    while (1);
  }
  
}

void loop()
{

  if (Serial.available() > 0)
  {
    inByte = Serial.read();
    switch (inByte) 
    {
      case HANDSHAKE:
        if (Serial.availableForWrite())
        {
          Serial.println("Message received");
        }
        break;
      case STREAM:
        printMag();
        break;
    }
  }
}