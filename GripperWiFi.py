import RPi.GPIO as GPIO          
from time import sleep
from flask import Flask
from flask import render_template


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



righten=GPIO.PWM(speedright,1000)
righten.start(25)
leften=GPIO.PWM(speedleft,1000)
leften.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low h-high e-exit")
print("\n")    



#remember to change name of webpage in return render!!!!
#remember to change the IP down below!!!!


@app.route('/')
def index():
    return render_template('Control_Interface.html')

@app.route('/fwd')
def led1on():
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/bckwd')
def led1off():
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')

@app.route('/left')
def led2on():
    GPIO.output(left1,GPIO.LOW)
    GPIO.output(left2,GPIO.HIGH)
    GPIO.output(right1,GPIO.HIGH)
    GPIO.output(right2,GPIO.LOW)
    return render_template('Control_Interface.html')

@app.route('/right')
def led2off():
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    GPIO.output(right1,GPIO.LOW)
    GPIO.output(right2,GPIO.HIGH)
    return render_template('Control_Interface.html')

@app.route('/makefast')
def led3on():
    leften.ChangeDutyCycle(75)
    righten.ChangeDutyCycle(75)
    return render_template('Control_Interface.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.1.57')  #enter IP of the PI here