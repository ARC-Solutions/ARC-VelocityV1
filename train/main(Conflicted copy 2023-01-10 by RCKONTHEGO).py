import serial
import time
import requests
from PIL import Image
from io import BytesIO
import uuid
import keyboard


arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# TODO: IMPORT FLASK & FLASK_CORS
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# start checking
# testTime = 1
# arduino.write(b'forward_on\n')
# time.sleep(testTime)
# arduino.write(b'forward_off\n')
# time.sleep(testTime)
# arduino.write(b'backward_on\n')
# time.sleep(testTime)
# arduino.write(b'backward_off\n')
# time.sleep(testTime)
# arduino.write(b'left_on\n')
# time.sleep(testTime)
# arduino.write(b'left_off\n')
# time.sleep(testTime)
# arduino.write(b'right_on\n')
# time.sleep(testTime)
# arduino.write(b'right_off\n')
# time.sleep(testTime)

dirDict = {
    '0': 'forward',
    '1': 'backwards',
    '2': 'left',
    '3': 'right'
}

def save_data(command):
    # request the image many times
    # for some reasons the app doesn't always return
    for _ in range(0, 10):
        response = requests.get('http://192.168.0.164:8080/shot.jpg')
    # save the image for future use
    # the direction is stored at the end of filename
    Image.open(BytesIO(response.content)).convert('L').save('images/{}_{}.jpg'.format(uuid.uuid1(), command))

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/forward")
def forward():
    #save_data(0)
    while True:
        try:
            if keyboard.is_pressed('w'):
                arduino.write(b'forward_on\n')
            else:
                arduino.write(b'forward_off\n')
            return 'forward'
        except:
            break

@app.route("/backward")
def backward():
    #save_data(1)
    while True:
        try:
            if keyboard.is_pressed('s'):
                arduino.write(b'backward_on\n')
            else:
                arduino.write(b'backward_off\n')
            return 'backward'
        except:
            break

@app.route("/left")
def left():
    #save_data(2)
    while True:
        try:
            if keyboard.is_pressed('a'):
                arduino.write(b'left_on\n')
            else:
                arduino.write(b'left_off\n')
            return 'left'
        except:
            break

@app.route("/right")
def right():
    #save_data(3)
    while True:
        try:
            if keyboard.is_pressed('d'):
                #arduino.write(b'forward_on\n')
                arduino.write(b'right_on\n')
            elif keyboard.is_pressed('f'):
                arduino.write(b'right_off\n')
                #arduino.write(b'forward_off\n')
        except:
            break
    return 'right'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

print("U good")

#     ____  ________ __
#    / __ \/ ____/ //_/
#   / /_/ / /   / ,<
#  / _, _/ /___/ /| |
# /_/ |_|\____/_/ |_|

