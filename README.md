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

Edit /boot/cmdline.txt and remove all options mentioning ttyAMA0. <br />
Edit /etc/inittab and comment out any lines mentioning ttyAMA0, especially the getty one. <br />
command to use for this is:
```
sudo nano *filemane*
```

and **Reboot** again!

### Schematic

The pdf file is the circuit you need to use to communicate with the AX12-A because the servo's use half-duplex communication and raspberry full-duplex. raspberry likes 3.3V and the servo's 5V.
With this circuit we solve all these problems!


## Functions

```
ping(self,id)
```
Does not command any operations. Used for requesting a status packet or to check the
existence of a Dynamixel actuator with a specific ID.
```
factoryReset(self,id, confirm = False)
```
Changes the control table values of the Dynamixel actuator to the Factory Default Value
settings

#### SetConfigValues
```
setID(self, id, newId)
```
It is a unique number to identify Dynamixel. </br>
The range from 0 to 252 (0xFC) can be used, and, especially, 254(0xFE) is used as the Broadcast ID.
If the Broadcast ID is used to transmit Instruction Packet, we can command to all Dynamixels.
```
setBaudRate(self, id, BaudRate)
```

It represents the communication speed. 0 to 254 (0xFE) can be used for it. </br>
This speed is calculated by using the below formula. </br>
Speed(BPS)  = 2000000/(Data+1)

| Data |  Set BPS   | Target BPS | Tolerance |
| ---- | ---------- | ---------- | --------- |
| 1    | 1000000.0  | 1000000.0  |  0.000 %  |
| 3    | 500000.0   | 500000.0   |  0.000 %  |
| 4    | 400000.0   | 400000.0   |  0.000 %  |
| 7    | 250000.0   | 250000.0   |  0.000 %  |
| 9    | 200000.0   | 200000.0   |  0.000 %  |
| 16   | 117647.1   | 115200.0   | -2.124 %  |
| 34   | 57142.9    | 576000.0   |  0.794 %  |
| 103  | 19230.8    | 192000.0   | -0.160 %  |
| 207  | 9615.4     | 9600.0     | -0.160 %  |

```
setReturnDelayTime(self, id, Delay)
```
It is the delay time per data value that takes from the transmission of Instruction Packet until the return of Status Packet. </br>
0 to 254 can be used, and the delay time per data value is 2 usec. </br>
That is to say, if the data value is 10, 20 usec is delayed. The initial value is 250 (i.e., 0.5 msec).

#### MoveServo
```
move(self, id, Position)
```
It is a position value of destination. </br>
0 to 1023 is available.  The unit is 0.29 degree. </br>
If Goal Position is out of the range, Angle Limit Error Bit (Bit1) of Status Packet is returned as ‘1’ and Alarm is triggered as set in Alarm LED/Shutdown.
```
moveSpeed(self, id, Position, Speed)
```
It is a moving speed to Goal Position.

The range and the unit of the value may vary depending on the operation mode.

* Join Mode </br>
0~1023 can be used, and the unit is about 0.111rpm. </br>
If it is set to 0, it means the maximum rpm of the motor is used without controlling the speed. </br>
If it is 1023, it is about 114rpm. </br>
For example, if it is set to 300, it is about 33.3 rpm.

*Notes: Please check the maximum rpm of relevant model in Joint Mode.  Even if the motor is set to more than maximum rpm, it cannot generate the torque more than the maximum rpm.*

* Wheel Mode </br>
0~2047 can be used, the unit is about 0.1%. </br>
If a value in the range of 0~1023 is used, it is stopped by setting to 0 while rotating to CCW direction. </br>
If a value in the range of 1024~2047 is used, it is stopped by setting to 1024 while rotating to CW direction. </br>
That is, the 10th bit becomes the direction bit to control the direction. </br>
In Wheel Mode, only the output control is possible, not speed. </br>
For example, if it is set to 512, it means the output is controlled by 50% of the maximum output.

```
moveRW(self, id, Position)
```
Same as function move it waits for an action
```
moveSpeedRW(self, id, Position, Speed)
```
Same as function moveSpeed it waits for an action
```
action(self)
```
All servos start there goal position with a speed if there is a speed specified.

#### SetLimits

```
setTemperatureLimit(self, id, Temp)
```
*Caution : Do not set the temperature lower/higher than the default value. When the temperature alarm shutdown occurs, wait 20 minutes to cool the temperature before re-use. Using the product when the temperature is high may and can cause damage.*

```
setVoltageLimit(self, id, Min_Volt, Max_Volt)
```
It is the operation range of voltage. </br>
setVoltageLimit(id, 50, 250) can be used.  The unit is 0.1V. </br>
For example, if the value is 80, it is 8V. </br>

If Present Voltage (Address42) is out of the range, Voltage Range Error Bit (Bit0) of Status Packet is returned as ‘1’ and Alarm is triggered as set in the addresses 17 and 18.

```
setAngleLimit(self, id, CW_Limit, CCW_Limit)
```
The angle limit allows the motion to be restrained. </br>
The range and the unit of the value is the same as Goal Position(Address 30, 31).

* CW Angle Limit: the minimum value of Goal Position(Address 30, 31)
* CCW Angle Limit: the maximum value of Goal Position(Address 30, 31)

The following two modes can be set pursuant to the value of CW and CCW.

| Operation Type | CW / CCW     |
| -------------- | ------------ |
| Wheel Mode     | both are 0   |
| Joint Mode     | neither at 0 |

The wheel mode can be used to wheel-type operation robots since motors of the robots spin infinitely. </br>
The joint mode can be used to multi-joints robot since the robots can be controlled with specific angles.

```
setTorqueLimit(self, id, Max_Torque)
```
It is the torque value of maximum output. </br>
0 to 1023  can be used, and the unit is about 0.1%. </br>
For example, Data 1023  means that Dynamixel will use 100% of the maximum torque it can produce while Data 512  means that Dynamixel will use 50% of the maximum torque. When the power is turned on, Torque Limit (Addresses 34 and 35) uses the value as the initial value.

```
setCompliance(self, id, cwMargin, ccwMargin, cwSlope, ccwSlope)
```

#### Alarm Table

| Bit   | Name | Contents |
| ----- | ---- | -------- |
| Bit 7 | 0 | - |
| Bit 6 | Instruction Error	| When undefined Instruction is transmitted or the Action command is delivered without the reg_write command |
| Bit 5 | Overload Error | When the current load cannot be controlled with the set maximum torque |
| Bit 4 | CheckSum Error | When the Checksum of the transmitted Instruction Packet is invalid
| Bit 3 | Range Error | When the command is given beyond the range of usage
| Bit 2 | OverHeating Error | When the internal temperature is out of the range of operating temperature set in the Control Table
| Bit 1 | Angle Limit Error	| When Goal Position is written with the value that is not between CW Angle Limit and CCW Angle Limit
| Bit 0 | Input Voltage Error	| When the applied voltage is out of the range of operating voltage set in the Control Table

#### ReadData
```
readTemperature(self, id)
```
Data value is identical to the actual temperature in Celsius. For example, if the data value is 85, the current internal temperature is 85℃
```
readPosition(self, id)
```
It is the current position value of Dynamixel. <br />  
The range of the value is 0~1023, and the unit is 0.29 degree.
```
readVoltage(self, id)
```
This value is 10 times larger than the actual voltage. For example, when 10V is supplied, the data value is 100
```
readSpeed(self, id)
```
If a value is in the rage of 0~1023, it means that the motor rotates to the CCW direction.<br />
If a value is in the rage of 1024~2047, it means that the motor rotates to the CW direction.
```
readLoad(self, id)
```
It means currently applied load. <br />
The range of the value is 0~2047, and the unit is about 0.1%. <br />
If the value is 0~1023, it means the load works to the CCW direction. <br />
If the value is 1024~2047, it means the load works to the CW direction. <br />
That is, the 10th bit becomes the direction bit to control the direction, and 1024 is equal to 0. <br />
For example, the value is 512, it means the load is detected in the direction of CCW about 50% of the maximum torque.
```
readMovingStatus(self, id)
```
0 = Goal position command execution is completed. <br />
1 = Goal position command execution is in progress.
```
readRWStatus(self, id)
```
0 = There are no commands. <br />
1 = There are commands.
