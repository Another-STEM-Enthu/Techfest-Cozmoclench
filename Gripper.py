import RPi.GPIO as GPIO          
from time import sleep



left1 = 23        #left motor direction
left2 = 24        #left motor direction

right1 = 14        #right motor direction
right2 = 15        #right motor direction

speedleft = 7      #left motor speed
speedright = 8     #right motor speed


go_forward = 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(left1,GPIO.OUT)
GPIO.setup(left2,GPIO.OUT)
GPIO.setup(right1,GPIO.OUT)
GPIO.setup(right2,GPIO.OUT)
GPIO.setup(speedleft,GPIO.OUT)
GPIO.setup(speedright,GPIO.OUT)


GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(go_forward==1):
         GPIO.output(left1,GPIO.HIGH)
         GPIO.output(left2,GPIO.LOW)
         GPIO.output(right1,GPIO.HIGH)
         GPIO.output(right2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(left1,GPIO.LOW)
         GPIO.output(left2,GPIO.HIGH)
         GPIO.output(right1,GPIO.LOW)
         GPIO.output(right2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
         GPIO.output(left1,GPIO.LOW)
         GPIO.output(left2,GPIO.LOW)
         GPIO.output(right1,GPIO.LOW)
         GPIO.output(right2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
         GPIO.output(left1,GPIO.HIGH)
         GPIO.output(left2,GPIO.LOW)
         GPIO.output(right1,GPIO.HIGH)
         GPIO.output(right2,GPIO.LOW)
        x='z'

    elif x=='b':
        print("backward")
         GPIO.output(left1,GPIO.LOW)
         GPIO.output(left2,GPIO.HIGH)
         GPIO.output(right1,GPIO.LOW)
         GPIO.output(right2,GPIO.HIGH)
        go_forward=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  INVALID COMMAND  >>>")
        print("Please enter a valid command.........")
