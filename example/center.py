import AX12
import time

servos = AX12.Ax12()
NUM_SERVO = 4
speed = 50
#print(servos.ping(5))

def mapdeg(x):
    return (int)((x - 30) * (1023 - 0) / (330 - 30));

for x in range(1, NUM_SERVO + 1):
    servos.moveSpeedRW(x, mapdeg(180), speed)
servos.action()
