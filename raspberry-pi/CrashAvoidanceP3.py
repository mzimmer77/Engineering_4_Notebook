# type: ignore

import terminalio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import digitalio
import board
import adafruit_mpu6050 
import busio
import time


displayio.release_displays()
i2c = busio.I2C(scl_pin, sda_pin) #
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP14)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area) 
display.show(splash)

sda_pin = board.GP14  #setting up my pins in the accelerometer 
scl_pin = board.GP15 #same thing
i2c = busio.I2C(scl_pin, sda_pin) # 
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
ledGreen = digitalio.DigitalInOut(board.GP0) # sets pin for green LED
ledRed = digitalio.DigitalInOut(board.GP1) # sets pin for red LED
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT 

while True:
    XAcceleration = mpu.acceleration[0] #explains the value of tuple for the different values 
    YAcceleration = mpu.acceleration[1] # for y
    ZAcceleration = mpu.acceleration[2] # for z

    print(f"X acceleration = {XAcceleration}") #prints the different values from the accelerometer
    print(f"Y acceleration = {YAcceleration}")
    print(f"Z acceleration = {ZAcceleration}")
    print("")

    time.sleep(.1) #just so it doesn't do it every .001 milisecond
    if ZAcceleration < 0:
        ledRed.value = True ## Turns on the Red LED
    else:
        ledRed.value = False #turns it off
        
    text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"

