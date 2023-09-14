# type: ignore
import digitalio 
import board
from time import sleep 
import pwmio
from adafruit_motor import servo

ledGreen = digitalio.DigitalInOut(board.GP0) # sets pin for green LED
ledRed = digitalio.DigitalInOut(board.GP1) # sets pin for red LED
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

Button = digitalio.DigitalInOut(board.GP3)#sets pin for button
Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP #internaly resists the button 

pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)


while True:
    if Button.value == False: 
        for x in range (10,0,-1): #using intervals that start at 10 and go to 0 with intervals every -1
            print (x) #prints my 
            ledRed.value = True #turns LED ON
            sleep (0.5)
            ledRed.value = False # TURNS LED OFF
            sleep (0.5) #counts down every second
        print ("we have liftoff") #prints we have liftoff
        servo1.angle = 0
        ledGreen.value = True
        sleep (3)
        ledGreen.value = False
        servo1.angle = 180