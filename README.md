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
I had to again use the previous code and I had to add in my srvo which I had to find the wiring to on [this website](https://docs.arduino.cc/learn/electronics/servo-motors). I had to bring it to 3.3v and I ended up using the 28th PWM port which just made the wiring look nicer. I learned that I had to put the servo angles to start at 0 so it wouldn't move until prompted at the end. I also used this part digitalio.Pull.UP because I changed where my GND was and where I was pulling from.

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
