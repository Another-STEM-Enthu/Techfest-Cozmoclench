import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
from flask import render_template

#check all pins once before testing/running anything!!!!!!!!!!!!!!!!!!

app= Flask(__name__)



grip = 32                    #for the grip servo!






GPIO.setmode(GPIO.BOARD)
GPIO.setup(grip,GPIO.OUT)



gripen=GPIO.PWM(grip,50)

gripen.start(2.5)

print("\n")
print("begin")
print("\n")



gripen.ChangeDutyCycle(2.5)
sleep(1)
#leften.ChangeDutyCycle(2.5)
#righten.ChangeDutyCycle(12.5)

#sleep(1)

gripen.stop()

