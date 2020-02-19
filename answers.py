"""Welcome to a THIS IS MY SPACESUIT. workshop!
This is the file you will use to code with your device.
There is pseudocode to give hints to the code.
After completing an example, you must comment out previous examples by using # on each line with code."""


"""EXAMPLE 1: CHECK CHECK. This example prints "THIS IS MY SPACESUIT. to the serial. Use the two lines of code below"""
from adafruit_circuitplayground import cp
print("THIS IS MY SPACESUIT.") #you can change the text to write whatever you want


"""EXAMPLE 2: RAINBOW MAGIC. This example lights up the first NeoPixel. The rest of the example will have you light up the entire board!"""

'''import statements - use 1 line of the code below'''
from adafruit_circuitplayground import cp


#'''#sets the brightness of the LEDs- use the code below'''
cp.pixels.brightness = 0.1

#to do: create a while loop that runs when it is true
while True:
#to do: access the first LED on the circle of your board - use the code below
    cp.pixels[0] = (255,0,0)
#to do: make more LEDs light up on the board by using the same notation as above. What will change? What color do you want to make?
    cp.pixels[1] = (50,20,0)
    cp.pixels[3] = (50,20,0)
'''EXAMPLE 3: I HAVE THE WORLD IN MY FINGERPRINTS.
This example lights up the entire board based on your touch'''

'''import statements - use 1 line of code below'''
from adafruit_circuitplayground import cp



'''sets the brightness of the LEDs- use the code below'''
cp.pixels.brightness = 0.1

#to do: create a while loop that runs when it is true
while True:
    # creates if statement if you touch the A1 port - use 1 line of code below
    if cp.touch_A1:
        #to do: fill all pixels to one color
        cp.pixels.fill(255)
    # to do: create an if statement if you touch the A2 port
    if cp.touch_A2: 
        #to do: fill all pixels to one color
        cp.pixels.fill(40)



'''EXAMPLE 4: DJ IN THE HOUSE.
This example plays a tone and shows an LED when you press a button'''

'''import statements - use 1 lines of code below'''
from adafruit_circuitplayground import cp



'''sets the brightness of the LEDs- use the code below'''
cp.pixels.brightness = 0.2

#to do: create a while loop that runs when it is true
while True:
    #to do: create an if statement for cp.button_a
    if cp.button_a:
        #to do: access the 1st pixel like example 3 and set a color to it
        cp.pixels[0] = (255,0,0)
        #to do: use cp.start_tone() to tell the device how long to ring a tone. Insert number from 0-200
        cp.start_tone(200)
    #to do: create an else statement
    else:
        #to do: access the 1nd pixel like example 3 and set the color to (0,0,0)
        cp.pixels[0] = (0,0,0)
        #stop the tone - use 1 line of the code below
        cp.stop_tone()


'''EXAMPLE 5: DISSOLVE IN SPACE .
This example should make the lights go on in a sequence. If you start with the first LED, it should stay on for a specific amount of time, then light up the next one. '''

'''import statements - use 1 lines of code below'''
from adafruit_circuitplayground import cp
import time

while True: 
    cp.pixels[0] = (200,0,0)
    time.sleep(2)
    cp.pixels[0] = (0,0,0)
    cp.start_tone(100)
    time.sleep(2)
    cp.stop_tone(100)
    time.sleep(2)
    #continue with other colors


#contact info:
# Instagram/Facebook: @thisismyspacesuit
# Email: thisismyspacesuit@gmail.com
# Website: thisismyspacesuit.com
