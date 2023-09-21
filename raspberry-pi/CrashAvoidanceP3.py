# type: ignore

import digitalio 
import adafruit_mpu6050
import busio
import board
import time 

sda_pin = board.GP14  #setting up my pins in the accelerometer 
scl_pin = board.GP15 #same thing
i2c = busio.I2C(scl_pin, sda_pin) # 
mpu = adafruit_mpu6050.MPU6050(i2c)
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

