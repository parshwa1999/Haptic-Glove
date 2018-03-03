
//#include <Mouse.h>

#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>

MPU6050 mpu;
int16_t ax, ay, az, gx, gy, gz;
int vx, vy;
int a1,a2;

void setup(){

  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  while (!mpu.testConnection()) { Serial.print("NOT Connected\n");  }
 //  Serial.println(F("\nSend any character to begin DMP programming and demo: "));
/*    while (Serial.available() && Serial.read()); // empty buffer
    while (!Serial.available());                 // wait for data
    while (Serial.available() && Serial.read()); // empty buffer again
*/
  //Serial.print("Connected");
}

void loop() {
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);


  vx = (gy+350)/200;
  vy = -(gz-100)/200;

  Serial.print("\n");
  Serial.print(vx);
  Serial.print(" ");
  Serial.print(vy);
 
/*  Serial.print("ax = ");
  Serial.print(gy);
  Serial.print(" | az = ");
  Serial.print(gz);
  Serial.print(" \n");
*/

  delay(50);
}


