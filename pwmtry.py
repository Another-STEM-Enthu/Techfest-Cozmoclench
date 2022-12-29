import RPi.GPIO as GPIO          
from time import sleep

frequency = 50   # in Hz   
dutycycle = 15    #the percent
pin       = 35    #motor pwm

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

#def startwheel(freq,duty):
#dutycycle = duty
T = 0.00
T = (1/frequency)
while(True):          
    
    GPIO.output(pin, GPIO.HIGH)
    sleep((dutycycle/100)*T)
    GPIO.output(pin,GPIO.LOW)
    sleep((1- dutycycle/100)*T)


    

