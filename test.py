from AX12 import *
import time

servos = AX12.Ax12()

while True:
    servos.moveSpeed(1, 256, 100)
    time.sleep(3)
    servos.moveSpeed(1, 768, 100)
    time.sleep(3)
