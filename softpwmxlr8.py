import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
from flask import render_template
import wheelpwm
#check all pins once before testing/running anything!!!!!!!!!!!!!!!!!!

app= Flask(__name__)

left1 = 24        #left motor direction
left2 = 23        #left motor direction

right1 = 15        #right motor direction
right2 = 16        #right motor direction

speedleft = 35      #left motor speed
speedright = 12     #right motor speed




GPIO.setmode(GPIO.BOARD)
GPIO.setup(left1,GPIO.OUT)
GPIO.setup(left2,GPIO.OUT)
GPIO.setup(right1,GPIO.OUT)
GPIO.setup(right2,GPIO.OUT)
GPIO.setup(speedleft,GPIO.OUT)
GPIO.setup(speedright,GPIO.OUT)



righten=GPIO.PWM(speedright,50)
righten.start(15)
leften=GPIO.PWM(speedleft,50)
leften.start(15)
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
    GPIO.output(right2, GPIO.LOW)
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

@app.route('/makefast')
def makefast():
    print("stop")
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2, GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/gup')
def gup():
    print('high speed!!!!!')
    leften.ChangeDutyCycle(80)
    righten.ChangeDutyCycle(80)
    return render_template('Control_Interface.html')

@app.route('/gdown')
def gdown():
    print('low speed')
    leften.ChangeDutyCycle(15)
    righten.ChangeDutyCycle(15)
    return render_template('Control_Interface.html')


if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.137.68')  #enter IP of the PI here
