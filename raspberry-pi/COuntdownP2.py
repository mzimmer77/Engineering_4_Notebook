# type: ignore
import time 
import digitalio 
import board

ledGreen = digitalio.DigitalInOut(board.GP0)# sets pin for green LED
ledRed = digitalio.DigitalInOut(board.GP1)# sets pin for red LED
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

for x in range (10,0,-1): #using intervals that start at 10 and go to 0 with intervals every -1
    print (x) #prints my 
    ledRed.value = True #turns LED ON
    time.sleep (0.5)
    ledRed.value = False # TURNS LED OFF
    time.sleep (0.5) #counts down every second
print ("we have liftoff") #prints we have liftoff
ledGreen.value = True #turns green LED on
time.sleep (1)