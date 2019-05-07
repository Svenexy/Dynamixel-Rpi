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
