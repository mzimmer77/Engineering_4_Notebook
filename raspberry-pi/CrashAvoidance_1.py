# type: ignore

import adafruit_mpu6050
import busio
import board
import time 

sda_pin = board.GP14  #setting up my pins in the accelerometer 
scl_pin = board.GP15 #same thing
i2c = busio.I2C(scl_pin, sda_pin) # 

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    XAcceleration = mpu.acceleration[0] #explains the value of tuple for the different values 
    YAcceleration = mpu.acceleration[1] # for y
    ZAcceleration = mpu.acceleration[2] # for z

    print(f"X acceleration = {XAcceleration}") #prints the different values from the accelerometer
    print(f"Y acceleration = {YAcceleration}")
    print(f"Z acceleration = {ZAcceleration}")
    print("")

    time.sleep(.25) #just so it doesn't do it every .001 milisecond