# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad Part 1](#Launchpad_P1)
* [Launchpad Part 2](#Launchpad_P2)
* [Launchpad Part 3](#Launchpad_P3)
* [Launchpad Part 4](#Launchpad_P4)
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launchpad_P1 

### Assignment Description

In Launch Pad Part 1, we had to countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor.

### Evidence 
![Something like this](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CountdownP1.gif.gif).

 

### Wiring

The wiring consisted of plugging the PICO board into my computer.

### Code

[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/launchpadP1.py)

### Reflection
This project was a great refresher for my python skills. I used the "for x in range (10,0,-1)" to make my intervals which would go down by 1. I learned/ remembered the syntax which was honestly annoying but it is pretty simple once you remember it (the key is to use commas for the loop).

&nbsp;

## Launchpad_P2

### Assignment Description

to have the serial monitor countdown from 10 to 0 by intervals of one and have a red LED blink the whole time every second. then when takeoff is initiated, A green LED should blink on.

### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/countdownP2gif.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/Countdown%20P2%20wiring.png)


### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/COuntdownP2.py).

### Reflection

Remembering how to wire even the leds was not easy so I asked google which yeilded positive results. I also had to use the right resistor which is the 220. Additionally,  using the right ports on the PICO is important. Make sure you put in the code to both put LEDs in and put them on the right ports.
&nbsp;


## Launchpad_P3

### Assignment Description

The assignment was to add a button to part 2 and to press the button then have the serial monitor count down from 10 while the red LED blinks every second.
### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/COuntdownP3.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CountdownP3%20Wiring.png)


### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchpadP3.py).

### Reflection
I was tasked with adding a button to the perious codes which again hung me up at first remembering how to wire up the button so I went on [this website](https://docs.arduino.cc/built-in-examples/digital/Button). I had to add my commands to bring the button into the code and give it both a PWM slot and a GND port. For the actual code  literally had to just add an IF loop so that when I pressed the button it would initiate the rest.

&nbsp;

## Launchpad_P4

### Assignment Description

The assignment was to add a servo to part 3 and make it rotate 180 degrees after the serial monitor printed "we have liftoff"
### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CountdownP4.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/Countdown%20P4%20Wiring.png)

### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/Countdown%20P4.py).

### Reflection
I had to again use the previous code and I had to add in my servo which I had to find the wiring to on [this website](https://docs.arduino.cc/learn/electronics/servo-motors). I had to bring it to 3.3v and I ended up using the 28th PWM port which just made the wiring look nicer. I learned that I had to put the servo angles to start at 0 so it wouldn't move until prompted at the end. I also used this part digitalio.Pull.UP because I changed where my GND was and where I was pulling from.

&nbsp;

## CrashAvoidanceP1

### Assignment Description

Our objective: wire up an accelerometer that returns acceleration values for the x, y, and z axes to the serial monitor. The units should be in m/s2.

### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CrashAvoidanceP1%20GIF.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CrashavoidanceP1%20wiring.png)


### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidance_1.py).

### Reflection
This assignment was difficult from the start but when I looked at the assignment on canvas it made it easier to wire up the gyroscope and I had to use the PWM pins GP14 and GP15 so that I had the I2C, SDA, and SCL so I could wire correctly. I had to use the mpu.acceleration with each value X,Y,Z so that I could get each value multiple times. Then all I did was print all my values with the print(f"X acceleration = {XAcceleration}") for X,Y,Z and I added a small sleep command so the values didn't come out too fast.

&nbsp;

## CrashAvoidanceP2

### Assignment Description

The assignment was to successfully set up an accelerometer. Then use those acceleration values to trigger a warning light if the helicopter is tilted at 90 degrees.
### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/CrashavoidanceP2%20GIF.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/Crashavoidance2Wriing.png)


### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidanceP2.pyy).

### Reflection
I made sure to use canvas fully so I could see the tips that Mr. Miller gave us which proves I am learning. I only really had to add in the LED which I just wired using any of my countdown projects. Additionally, I used the if ZAcceleration < 0 so that whenever it flips over the LED turns on using a true false statement. I also changed the time.sleep multiple times in order to get the best results which I got at 0.1 seconds.

&nbsp;


## CrashAvoidanceP3

### Assignment Description

You have successfully set up an accelerometer and made your device mobile. Now you will add an onboard OLED screen to print live angular velocity values.

### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/crashavoidancegifP3.gif)

### Wiring

![My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/crashavoidancewirigP3.png)


### Code
[My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidanceP3.py).

### Reflection

I had to first figure out how to wire up the OLED screen and I used the same pins as I used for my other I2C device. This also meant that I had to find both I2C devices addresses using the code from onshape. Then I used another part of the code from canavs to set up what my board color was and where the values showed up. The syntax was also important because where you have to define your SCL and SDA pins are very important.

&nbsp;


## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

![My GIF](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/countdownP2gif.gif)

### Wiring

[My wiring](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/launchpadpart2wiringdiagram.png)


### Code
![My Code](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/raspberry-pi/COuntdownP2.py).

### Reflection


&nbsp;




## FEA Part one

### Assignment Description

We had to create a beam that was less than or equal to 13 grams and try to make it able to hold as much weight as possible.
### Part Link 

[Link to Onshapet](https://cvilleschools.onshape.com/documents/24b88ffe9264a0c98a74dc0e/w/222f8de2303c65f5e9c59127/e/16bf75dd5e63ea4c1d80e02d). 

### Part Image

![Nice Screenshot](https://github.com/mzimmer77/Engineering_4_Notebook/blob/main/images/FEA%20BEAM%20PART%20ONE.png)
### Reflection

This project made me and Vinnie learn to work as a team together. we both have good ideas and it is hard to choose the best one sometimes it leads to arguments but in the end, we prevailed and came up with a great design that will hopefully hold up lots of weight (more than just the bucket). I also relearned lots of things in CAD such as what the chamfer tool does and just some basics that I hadn't used in 4 months. We used variables and design intent to make editing the beam easier. this made me want to kill myself over and over


&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!


### Test Link
[Hyperlink text](http://www.google.com)      

### Test Image
![bigD](images/thebigd2.png)
### Test GIF
![its-friday-dancing](https://github.com/mzimmer77/Engineering_4_Notebook/assets/112961434/42d6898b-dee3-4c53-982f-c75a0a9f01fd)
