# Library to work with serial data
import serial

# Library for String manipulation
import re

# Library for system function usage
import sys

# Library move mouse pointer in python
import pyautogui    

# Execption handling
try:
	# To select Serial port	
	arduino = serial.Serial("/dev/ttyACM0",timeout=1)
	
	# Forever while loop
	while True:
    
	# Initialize string values to be read
	str1 = [0,0]
	str2 = [0,0]
    
	# Read data serially from given port and manipulate string data
	a1 = str(arduino.readline())
	a2 = str(arduino.readline())

	# To manipulate String and trim off other data
	if(a1[2] == 'X'):
		str1 = [int(s) for s in re.findall(r'-?\d+\.?\d*', a1)]
       # Else skip line
	else:
		arduino.readline()

       # To manipulate String and trim off other data
	if(a2[2] == 'Y'):
		str2 = [int(s) for s in re.findall(r'-?\d+\.?\d*', a2)]


	# Move mouse Relatively by mapping the values given by MPU6050 and calibrate it
	pyautogui.moveRel((str2[0] )*2, (-2*(str1[0] )), duration = 0.01)

	#print all values of sensors
	print(str2[0] )
	print(-1*(str1[0] ))
	print(str2[0])

	# Check is pointer clicked
	if(str2[1] == 1):
		pyautogui.click(pyautogui.position())
     
# Trying to catch an exception    
except:
	print('check')

