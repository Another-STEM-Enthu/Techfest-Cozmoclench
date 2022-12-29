import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
from flask import render_template

#check all pins once before testing/running anything!!!!!!!!!!!!!!!!!!

app= Flask(__name__)



left = 35                    #for the servo!
right = 12                    #for the servo!






GPIO.setmode(GPIO.BOARD)
GPIO.setup(left,GPIO.OUT)
GPIO.setup(right,GPIO.OUT)



leften=GPIO.PWM(left,50)
righten=GPIO.PWM(right,50)

leften.start(7.5)
righten.start(7.5)

print("\n")
print("begin")
print("\n")



#going down
angle_left = 90 - 10
angle_right = 90 + 10


GPIO.output(left, True)
leften.ChangeDutyCycle((angle_left/18) + 2.5)
righten.ChangeDutyCycle((angle_right/18) + 2.5)
sleep(1)
GPIO.output(left, False)
GPIO.output(right, False)
leften.ChangeDutyCycle(0)
righten.ChangeDutyCycle(0)
#leften.ChangeDutyCycle(2.5)
#righten.ChangeDutyCycle(12.5)

#sleep(1)

leften.stop()
righten.stop()

