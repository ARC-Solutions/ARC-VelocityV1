import serial
import time
import requests
from PIL import Image
from io import BytesIO
import uuid
import keyboard
from concurrent.futures import ThreadPoolExecutor

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

# def save_data(command):
#     # request the image many times
#     # for some reasons the app doesn't always return
#     for _ in range(0, 10):
#         response = requests.get('CameraURL')
#     # save the image for future use
#     # the direction is stored at the end of filename
#     Image.open(BytesIO(response.content)).convert('L').save('images/{}_{}.jpg'.format(uuid.uuid1(), command))

executor = ThreadPoolExecutor(max_workers=2)
f1 = executor.submit(app.route, '/forward')
f2 = executor.submit(app.route, '/backward')
# f3 = executor.submit(app.route, '/left')
# f4 = executor.submit(app.route, '/right')
f1.result()
f2.result()
# f3.result()
# f4.result()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/forward")
def forward():
    # save_data(0)
    try:
        while True:
            if keyboard.is_pressed('w') and keyboard.is_pressed('d'):
                # print('goes forward and to the right')
                arduino.write(b'forward_on\n')
                arduino.write(b'right_on\n')
            elif keyboard.is_pressed('w') and keyboard.is_pressed('a'):
                arduino.write(b'forward_on\n')
                arduino.write(b'left_on\n')
                # print('goes forward and to the left')
            elif keyboard.is_pressed('w') and not keyboard.is_pressed('d'):
                arduino.write(b'forward_on\n')
                arduino.write(b'right_off\n')
                arduino.write(b'left_off\n')
                # print('goes forward')

            elif not keyboard.is_pressed('w'):
                arduino.write(b'forward_off\n')
                arduino.write(b'left_off\n')
                arduino.write(b'right_off\n')
                # print('doesnt go anywhere')
                break
        return 'forward'
    except serial.SerialTimeoutException:
        pass

@app.route("/backward")
def backward():
    # save_data(1)
    try:
        while True:
            if keyboard.is_pressed('s') and keyboard.is_pressed('d'):
                arduino.write(b'backward_on\n')
                arduino.write(b'right_on\n')
                # print('goes backward and to the right')

            elif keyboard.is_pressed('s') and keyboard.is_pressed('a'):
                arduino.write(b'backward_on\n')
                arduino.write(b'left_on\n')
                # print('goes backward and to the left')

            elif keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
                arduino.write(b'backward_on\n')
                arduino.write(b'right_off\n')
                arduino.write(b'left_off\n')
                # print('goes backward')

            elif not keyboard.is_pressed('s'):
                arduino.write(b'backward_off\n')
                arduino.write(b'left_off\n')
                arduino.write(b'right_off\n')
                # print('car dont go')
                break
        return 'backward'
    except serial.SerialTimeoutException:
        pass

# @app.route("/left")
# def left():
#     #save_data(2)
#     while True:
#         if keyboard.is_pressed('a'):
#             arduino.write(b'left_on\n')
#         elif not keyboard.is_pressed('a'):
#             arduino.write(b'left_off\n')
#             break
#     return 'left'
#
# @app.route("/right")
# def right():
#     #save_data(3)
#     while True:
#         if keyboard.is_pressed('d'):
#             arduino.write(b'right_on\n')
#         elif not keyboard.is_pressed('d'):
#             arduino.write(b'right_off\n')
#             break
#     return 'right'

with app.test_client() as client:
    response = client.get('/forward')
    # response = client.get('/right')
    # response = client.get('/left')
    response = client.get('/backward')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

print("U good")

#     ____  ________ __
#    / __ \/ ____/ //_/
#   / /_/ / /   / ,<
#  / _, _/ /___/ /| |
# /_/ |_|\____/_/ |_|
