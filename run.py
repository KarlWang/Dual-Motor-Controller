from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO
from Raspi_MiniMoto_Driver import MOTO
import time

MY_GPIO_18 = 18
motor1 = MOTO(0x60)
motor2 = MOTO(0x65)

app = Flask(__name__)
@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)

@app.route("/led/<On_Off>")
def led_on_off(On_Off):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MY_GPIO_18, GPIO.OUT)
    if On_Off == 'on':
        GPIO.output(MY_GPIO_18, GPIO.HIGH)
        return 'LED ON!!'
    elif On_Off == 'off':
        GPIO.output(MY_GPIO_18, GPIO.LOW)
        GPIO.cleanup()
        return 'LED OFF!!'
    else:
        GPIO.cleanup()
        return 'Invalid argument!'

@app.route('/ledoff')
def led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MY_GPIO_18, GPIO.OUT)
    return 'LED OFF!!'

@app.route('/motors_con/<Left_Right>')
def motors_con(Left_Right):
    L_R = Left_Right.split("+")
    iL = int(L_R[0])
    iR = int(L_R[1])

    if iL > 0:
        motor1.drive(40)
    elif iL < 0:
        motor1.drive(-40)
    else:
        motor1.brake()

    if iR > 0:
        motor2.drive(40)
    elif iR < 0:
        motor2.drive(-40)
    else:
        motor2.brake()
    
    return Left_Right

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
