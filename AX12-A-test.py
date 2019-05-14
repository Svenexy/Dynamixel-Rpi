#from AX12 import *
import AX12
import time

servos = AX12.Ax12()
speed = 100
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
