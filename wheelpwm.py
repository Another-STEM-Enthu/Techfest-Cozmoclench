import RPi.GPIO as GPIO          
from time import sleep

frequency = 50   # in Hz   
dutycycle = 15    #the percent
pin       = 13    #motor pwm

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

#def startwheel(freq,duty):
#dutycycle = duty
T = 0.00
T = (1/frequency)*1000 #in ms
while(True):          
    value = int((dutycycle/100)*T)
    #iterate for time period by 1ms 
    for i in range(1,int(T)):    #every iteration of for is 1ms
        if(i <= value):
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin,GPIO.LOW)
        sleep(0.001)


    

