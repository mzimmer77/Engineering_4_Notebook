# type: ignore
import time 
import digitalio 
import board

ledGreen = digitalio.DigitalInOut(board.GP0)
ledRed = digitalio.DigitalInOut(board.GP1)
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

for x in range (10,0,-1): #using intervals that start at 10 and go to 0 with intervals every -1
    print (x) #prints my 
    ledRed.value = True
    time.sleep (0.5)
    ledRed.value = False
    time.sleep (0.5) #counts down every second
print ("we have liftoff") #prints we have liftoff
ledGreen.value = True
time.sleep (1)