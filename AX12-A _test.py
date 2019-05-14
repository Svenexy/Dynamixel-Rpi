'''
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
 
port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
     
while True:
        GPIO.output(18, GPIO.HIGH)
        #port.write(bytearray.fromhex("FF FF 01 05 03 1E 32 03 A3"))
        #port.write(bytearray.fromhex("FF FF 02 05 03 1E 32 03 A2"))
        port.write(bytearray.fromhex("FF FF 03 05 03 1E 32 03 A1"))
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(3)

        GPIO.output(18,GPIO.HIGH)
        #port.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 0b"))
        #port.write(bytearray.fromhex("FF FF 02 05 03 1E CD 00 0a"))
        port.write(bytearray.fromhex("FF FF 03 05 03 1E CD 00 09"))
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(3)
        
'''
#from AX12 import *
import AX12
import time

servos = AX12.Ax12()
speed = 75
#print(servos.ping(5))

def mapdeg(x): 
    return (int)((x - 30) * (1023 - 0) / (330 - 30));




while True:
    servos.moveSpeedRW(1, mapdeg(90), speed)
    servos.moveSpeedRW(4, mapdeg(270), speed)
    servos.moveSpeedRW(3, mapdeg(90), speed)
    servos.moveSpeedRW(2, mapdeg(270), speed)
    servos.action()
    print('Tempurture Servos: ')
    for x in range(1,5):
        print('Servo ' + str(x) + ' temp: ' + str(servos.readTemperature(x)) + ' °C')
        time.sleep(0.75)
    servos.moveSpeedRW(1, mapdeg(270), speed)
    servos.moveSpeedRW(4, mapdeg(90), speed)
    servos.moveSpeedRW(3, mapdeg(270), speed)
    servos.moveSpeedRW(2, mapdeg(90), speed)
    servos.action()
    time.sleep(3)
    
    
    
    
    
    



