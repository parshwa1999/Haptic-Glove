#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
MPU6050 mpu;
// 16 bits variables to get values of accelerometer and gyroscope in X, Y and Z axis.
int16_t ax, ay, az, gx, gy, gz;
// Variables in X direction and Y direction.
int vx, vy;
// Buttons for left and right click.
int button1 = 6;
int button2 = 7;
int buttonState1 = 0;
int buttonState2 = 0;
int leftButton;

void setup() {
	// To Initialize the Serial Bus for printing data.
	Serial.begin(9600);
	
	/*
	* To initiate the Wire library and join the I2C bus as a master or slave.
	* This function should normally be called only once.
	*
	* Parameters :- address: the 7-bit slave address (optional); if not specified, join the bus as a master.
	*
	* Returns :- None
	*/
	
	Wire.begin();
	
	//Buttons used for clicking
	pinMode(button1, INPUT);
	pinMode(button2, INPUT);
	pinMode(7, INPUT);
	
	// To initialize MPU 6050 with default values
	mpu.initialize();

	// Wait for MPU6050 to respond test connection function tries to recieve demo data to check is MPU6050 connected perfectly
	if (!mpu.testConnection()) { while (1); }
}
void loop() {

	// Function used to get values of accelerometer and gyroscope in three directions.
	mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

	// Calculate velocities in X and Y directions
	vx = (gx+15)/150;
	vy = -(gz-100)/150;

	// Read data from pin7 to check has user clicked
	leftButton = digitalRead(7);
	delay(100);

	// Delay to stop switch Debouncing.
	// Print data serially along X axis
	Serial.print("X");
	Serial.println(vx+4);

	// added values to calibrate sensors value
	delay(100);

	//Delay kept for instructions not to be skipped
	Serial.print("Y");

	Serial.print(vy-1);
	delay(100);

	// added values to calibrate the sensors value
	//Delay kept for instructions not to be skipped
	// When Switch is pressed low voltage (low logic level) is passed
	//To check and print on serial monitor that is PIN high or low i.e. is switched pressed or not
	if(leftButton == HIGH){
		Serial.println(" 0");
		delay(100);
	}
	if(leftButton == LOW){
		Serial.println(" 1");
		delay(100);
	}
}
