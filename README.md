# Dynamixel-Rpi

This library is for communication with the Dynamixel AX12-A (i dont know for the other Dynamixel series!)

## Getting Started

First of al we need to change some config settings in the Raspberry Pi

### UART AND CORE_FREQ

Open the terminal on the raspberry and run this command:
```
sudo nano /boot/config.txt
```
After that you need to add this in the file:
```
#AX12-A
init_uart_clock=16000000
enable_uart=1
```
This is for enabling the serial port of the Raspberry at a baudrate of 16000000.
But the Raspberry loves to change his core frequency and with that he is also changing the baudrate to fix this at under arm_freq=800:
```
core_freq=400
```

Press CTRL-X and say YES, and **Reboot**

### Set other parameters

Run this command:
```
sudo stty -F /dev/ttyAMA0 1000000
```

Edit /boot/cmdline.txt and remove all options mentioning ttyAMA0.
Edit /etc/inittab and comment out any lines mentioning ttyAMA0, especially the getty one.
command to use for this is:
```
sudo nano *filemane*
```

and **Reboot** again!

### Schematic

The pdf file is the circuit you neet to use to comminucate with the AX12-A becuase the servo's use half-duplex communication and raspberry full-duplex. raspberry likes 3.3V and the servo's 5V.
With this cicuit we solve all these problems!
<<<<<<< HEAD
<<<<<<< HEAD


## Functions

```
ping(self,id)
factoryReset(self,id, confirm = False)
```

```
setID(self, id, newId)
setBaudRate(self, id, BaudRate)
setStatusReturnLevel(self, id, Level)
setReturnDelayTime(self, id, Delay)
lockRegister(self, id)
```

```
move(self, id, Position)
moveSpeed(self, id, Position, Speed)
moveRW(self, id, Position)
moveSpeedRW(self, id, Position, Speed)
action(self)
```

```
setTorqueStatus(self, id, Status)
setLedStatus(self, id, Status)
setTemperatureLimit(self, id, Temp)
setVoltageLimit(self, id, Min_Volt, Max_Volt)
setAngleLimit(self, id, CW_Limit, CCW_Limit)
setTorqueLimit(self, id, Max_Torque)
setPunchLimit(self, id, Punch)
setCompliance(self, id, cwMargin, ccwMargin, cwSlope, ccwSlope)
```

```
setLedAlarm(self, id, Alarm)
setShutdownAlarm(self, id, Alarm)
```

```
readTemperature(self, id)
Data value is identical to the actual temperature in Celsius. For example, if the data value is 85, the current internal temperature is 85℃

readPosition(self, id)
It is the current position value of Dynamixel.  
The range of the value is 0~1023, and the unit is 0.29 degree.

readVoltage(self, id)
This value is 10 times larger than the actual voltage. For example, when 10V is supplied, the data value is 100

readSpeed(self, id)
If a value is in the rage of 0~1023, it means that the motor rotates to the CCW direction.
If a value is in the rage of 1024~2047, it means that the motor rotates to the CW direction.

readLoad(self, id)
It means currently applied load.
The range of the value is 0~2047, and the unit is about 0.1%.
If the value is 0~1023, it means the load works to the CCW direction.
If the value is 1024~2047, it means the load works to the CW direction.
That is, the 10th bit becomes the direction bit to control the direction, and 1024 is equal to 0.
For example, the value is 512, it means the load is detected in the direction of CCW about 50% of the maximum torque.

readMovingStatus(self, id)
0 = Goal position command execution is completed.
1 = Goal position command execution is in progress.

readRWStatus(self, id)
0 = There are no commands.
1 = There are commands.


```
