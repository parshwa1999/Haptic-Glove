import serial

try:
	arduino = serial.Serial("/dev/ttyACM0",timeout=1)
	while True:
		a1 = str(arduino.readline())
		print(a1)
except:
	print('check')
	
#while True:
#	a = str(arduino.readline())
#	print(a)



