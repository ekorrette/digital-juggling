//Gravity Acceleration
#include "LIS3DHTR.h"
#ifdef SOFTWAREWIRE
  #include <SoftwareWire.h>
  SoftwareWire myWire(3, 2);
  LIS3DHTR<SoftwareWire> LIS;//IIC
  #define WIRE myWire
#else
  #include <Wire.h>
  LIS3DHTR<TwoWire> LIS;//IIC
  #define WIRE Wire
#endif


int counter = 0;
bool flight = false;
int thresh = 50;
float eps = 0.1;

void setup() {
  Serial.begin(9600);
  while (!Serial) {};
  LIS.begin(WIRE, 0x19); //IIC init
  delay(100);
  LIS.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);
}

void loop() {
  if (!LIS) {
  Serial.println("LIS3DHTR didn't connect.");
  while (1);
  return;
 }
 //3 axis
//  Serial.print(LIS.getAccelerationX()); Serial.print(" ");
//  Serial.print(LIS.getAccelerationY()); Serial.print(" ");
//  Serial.println(LIS.getAccelerationZ());

  float x = LIS.getAccelerationX();
  float y = LIS.getAccelerationY();
  float z = LIS.getAccelerationZ();

  float acc = x*x + y*y + z*z;




  if (acc < eps) {
    if (!flight) {
      if (counter < thresh) {
        counter++;
      } else {
        flight = true;
        Serial.write(1);
        counter = 0;
      }
    }
  } else {
    if (flight) {
      if (counter < thresh) {
        counter++;
      } else {
        flight = false;
        counter = 0;
      }
    } 
  }

  delay(2);
}
