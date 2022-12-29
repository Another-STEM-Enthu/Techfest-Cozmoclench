import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
from flask import render_template

#check all pins once before testing/running anything!!!!!!!!!!!!!!!!!!

app= Flask(__name__)

left1 = 24        #left motor direction
left2 = 23        #left motor direction

right1 = 15        #right motor direction
right2 = 16        #right motor direction


wheel_en = 18     #motor speed
grip = 32         #for the grip servo!

left = 35                    #for the lower-raise servo!
right = 12                   #for the lower-raise servo!


GPIO.setmode(GPIO.BOARD)
GPIO.setup(left1,GPIO.OUT)
GPIO.setup(left2,GPIO.OUT)
GPIO.setup(right1,GPIO.OUT)
GPIO.setup(right2,GPIO.OUT)
GPIO.setup(wheel_en,GPIO.OUT)
GPIO.setup(grip,GPIO.OUT)
GPIO.setup(left,GPIO.OUT)
GPIO.setup(right,GPIO.OUT)



wheels=GPIO.PWM(wheel_en,50)
wheels.start(15)
gripen=GPIO.PWM(grip,50)
gripen.start(0)
leften=GPIO.PWM(left,50)
leften.start(7.5)
righten=GPIO.PWM(right,50)
righten.start(7.5)
print("\n")
print("begin")
print("\n")



#remember to change name of webpage in return render!!!!
#remember to change the IP down below!!!!


@app.route('/')
def index():
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/fwd')
def fwd():
    print('fwd')
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')


@app.route('/bckwd')
def bckwd():
    print('bckwd')
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')

@app.route('/left')
def left():
    print('left')
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/right')
def right():
    print('right')
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')


@app.route('/stop')
def makefast():
    print("stop")
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2, GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/gup')
def gup():
    print('gripper raise')
    leften.ChangeDutyCycle(12.5)
    righten.ChangeDutyCycle(2.5)
    return render_template('Control_Interface.html')

@app.route('/gdown')
def gdown():
    print('gripper lower')
    leften.ChangeDutyCycle(7.5)
    righten.ChangeDutyCycle(7.5)
    return render_template('Control_Interface.html')

@app.route('/gopen')
def gopen():
    print('gripper open')
    gripen.ChangeDutyCycle(2.5)
    sleep(0.5)
    return render_template('Control_Interface.html')

@app.route('/gclose')
def gclose():
    print('gripper close')
    gripen.ChangeDutyCycle(5.83)
    sleep(0.5)
    return render_template('Control_Interface.html')

#speed modes
@app.route('/speed1')
def gclose():
    print('speed1')
    wheels.ChangeDutyCycle(20)
    sleep(0.5)
    return render_template('Control_Interface.html')
@app.route('/speed2')
def gclose():
    print('speed2')
    wheels.ChangeDutyCycle(50)
    sleep(0.5)
    return render_template('Control_Interface.html')
@app.route('/speed3')
def gclose():
    print('speed3')
    wheels.ChangeDutyCycle(85)
    sleep(0.5)
    return render_template('Control_Interface.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.137.180')  #enter IP of the PI here
