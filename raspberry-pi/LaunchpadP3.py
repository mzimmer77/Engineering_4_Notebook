# type: ignore
import time 
import digitalio 
import board
from time import sleep 

ledGreen = digitalio.DigitalInOut(board.GP0) # sets pin for green LED
ledRed = digitalio.DigitalInOut(board.GP1) # sets pin for red LED
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

Button = digitalio.DigitalInOut(board.GP3)#sets pin for button
Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.DOWN #internaly resists the button 


while True:
    if Button.value == True: 
        for x in range (10,0,-1): #using intervals that start at 10 and go to 0 with intervals every -1
            print (x) #prints my 
            ledRed.value = True #turns LED ON
            time.sleep (0.5)
            ledRed.value = False # TURNS LED OFF
            time.sleep (0.5) #counts down every second
        print ("we have liftoff") #prints we have liftoff
        ledGreen.value = True
        time.sleep (1)
