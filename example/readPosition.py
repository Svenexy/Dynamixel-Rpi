import AX12
import time

servos = AX12.Ax12()

while True:

    print('Temperature Servos: ')
    for x in range(1,5):
        print('Servo ' + str(x) + ' temp: ' + str(servos.readTemperature(x)))
        time.sleep(0.75)
