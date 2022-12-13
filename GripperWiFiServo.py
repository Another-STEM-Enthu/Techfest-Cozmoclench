import RPi.GPIO as GPIO          
from time import sleep
from flask import Flask
from flask import render_template

#check all pins once before testing/running anything!!!!!!!!!!!!!!!!!!

left1 = 23        #left motor direction
left2 = 24        #left motor direction

right1 = 14        #right motor direction
right2 = 15        #right motor direction

speedleft = 7      #left motor speed
speedright = 8     #right motor speed

#these are hardware pwm pins
servo_oc = 32      #to open/close the grip
servotilt = 33     #to tilt the gripper config


GPIO.setmode(GPIO.BOARD)
GPIO.setup(left1,GPIO.OUT)
GPIO.setup(left2,GPIO.OUT)
GPIO.setup(right1,GPIO.OUT)
GPIO.setup(right2,GPIO.OUT)
GPIO.setup(speedleft,GPIO.OUT)
GPIO.setup(speedright,GPIO.OUT)
GPIO.setup(servo_oc,GPIO.OUT)
GPIO.setup(servotilt,GPIO.OUT)




# righten=GPIO.PWM(speedright,50)
# righten.start(25)
# leften=GPIO.PWM(speedleft,50)
# leften.start(25)

gripen = GPIO.PWM(servo_oc,50)
gripen.start(0)
tilten = GPIO.PWM(servo_oc,50)
tilten.start(0)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low h-high e-exit")
print("\n")    

def speed_tune(pin,percent,freq):   #freq is in Hz
    for i in range(0,):
        GPIO.output(pin,1)

        sleep(1/freq)

def openclose(angle):
	duty = (angle/18) + 2.5
	GPIO.output(servo_oc, 1)
	gripen.ChangeDutyCycle(duty)
	sleep(1.5)                          #time is in seconds!!!!!! Check if this is sufficient/excess!!
	GPIO.output(servo_oc, 0)
	gripen.ChangeDutyCycle(0)

def updown(angle):
	duty = (angle/18) + 2.5
	GPIO.output(servo_oc, 1)
	tilten.ChangeDutyCycle(duty)
	sleep(1.5)                          #time is in seconds!!!!!! Check if this is sufficient/excess!!
	GPIO.output(servo_oc, 0)
	tilten.ChangeDutyCycle(0)

#remember to change name of webpage in return render!!!!
#remember to change the IP down below!!!!


@app.route('/')
def index():
    return render_template('Control_Interface.html')

@app.route('/fwd')
def fwd():
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/bckwd')
def bckwd():
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')

@app.route('/left')
def left():
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/right')
def right():
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')

@app.route('/makefast')
def makefast():
    leften.ChangeDutyCycle(75)
    righten.ChangeDutyCycle(75)
    return render_template('Control_Interface.html')

@app.route('/gopen')
def gopen():
    openclose(120)
    return render_template('webpage.html')

@app.route('/gclose')
def gclose():
    openclose(60)                               #need to manually check and adjust this
    return render_template('webpage.html')

@app.route('/gup')
def gup():
    updown(100)
    return render_template('webpage.html')

@app.route('/gopen')
def gopen():
    updown(0)
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.1.57')  #enter IP of the PI here


'''
Reference : https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/
from https://components101.com/motors/mg995-servo-motor,
the Time period of the servo is 20 ms;
and 0.5ms of PWM means servo @ 0 degrees;
and there is a 10% delta for the duty cycle, i.e 0.5ms + (0 to 2ms) => 2.5% is 0 degrees and (2.5+10)% is 180 and (2.5 + 5)% is 90 degree
input to the PWM() function is the duty cycle

Use pwm.start(0) so that motor is at 0 degrees angle on bootup
so, to rotate to x degress, we need to give argument to PWM() function as = 2.5 + (x/18)
remember to keep a delay of about 1-2s after the PWM function to allow the servo to complete its rotation using sleep(<time in s>)
After sleep(), do:
GPIO.output(03, False)
pwm.ChangeDutyCycle(0)
so that we don't continuously send inputs to the servo
'''

