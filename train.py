import pyfirmata as fir
import time 

arduino = fir.Arduino('COM4')
arduino.digital[9].mode = fir.OUTPUT
arduino.digital[9].write(1)