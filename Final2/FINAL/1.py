#!/bin/python

import sys
import pyautogui
import serial
from decimal import Decimal

try:
    arduino = serial.Serial("/dev/ttyACM0",timeout=1)
except:
    print('check')

#while True:
#    a = str(arduino.readline())
#    print(a)


while True:
    a1 = str(arduino.readline())
    a2 = str(arduino.readline())
    a3 = str(arduino.readline())
    a4 = str(arduino.readline())    
#    a = '308 766\n'
#    print('a = '+a)

    print(a1)
    print(a2)
    print(a3)
    print(a4)

    if(a2[2]!='y'):
        a2=str(arduino.readline())
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        continue

    if(a3[2]!='u'):
#        a2=str(arduino.readline())
        print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        continue

    if(a4[2]!='v'):
#        a2=str(arduino.readline())
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        continue


    a1+='aaa'
    a2+='aaa'

    x='0'
    i=2
    while (a1[i].isdigit()):
        x += a1[i]
        i=i+1

    i=i+1
    x+='.'

    while (a1[i].isdigit()):
        x += a1[i]
        i=i+1

#    print(x)

    y='0'
    i=3
    while (a2[i].isdigit()):
        y += a2[i]
        i=i+1

    i=i+1
    y+='.'

    while (a2[i].isdigit()):
        y += a2[i]
        i=i+1
#    print(y)

    x = float(x)
    y = float(y)

#    print(y)
#    print('jjj')
#    print(x, y)

    x1=0
    y1=0

    if(x>=0 and x <=180):
        x = x
    elif(x>=180 and x <=360):
        x = x-360

    if(y>=0 and y <=180):
        y = y
    elif(y>=180 and y <=360):
        y = y-360

    y1 = (6.3833*round((x/1.7),0)*3.4) + 384
    x1 = (17.075*round((y/1.7),0)*3.4) + 683
#    print('ddd')
#    print(x1, y1)
    if (x1!=0 or y1!=0):
        pyautogui.moveTo(x1, y1, duration=0.025)
    else:
        pyautogui.moveTo(1, 1, duration=0.025)


    if((a3[3])=='1'):
        print("CCCCCCCCCCCCllLlllllllllliiiiiiiiiicccccccccccccckkkkkkkkkkk")
        pyautogui.click(pyautogui.position())

    if((a4[3])=='1'):
        print("RRRRRRRRRRRRRRRRRRRRRRRRRCCCCCCCCCCCCllLlllllllllliiiiiiiiiicccccccccccccckkkkkkkkkkk")
        pyautogui.dragRel(-250,250, duration=3)
        pyautogui.dragRel(-250,-250, duration=3)





