import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.out)

GPIO.output(4,True)
time.sleep(1)
GPIO.output(4,False)
