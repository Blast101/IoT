import RPi.GPIO as GPIO
import time
import datetime
from flask import Flask, render_template

led = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT, initial=0)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('web6.html')

@app.route('/redledon')
def redledon():
    GPIO.output(led, GPIO.LOW)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
        'status' : 'ON',
        'time' : timeString
    }
    return render_template('web.html', **templateData)

@app.route('/redledoff')
def redledoff():
    GPIO.output(led, GPIO.HIGH)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
        'status' : 'OFF',
        'time' : timeString
    }
    return render_template('web.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)