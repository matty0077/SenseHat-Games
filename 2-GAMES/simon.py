#import numpy as np
import time
import pandas as pd
from math import*
import random
from sense_hat import SenseHat
sense = SenseHat()


r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255,255,255]
z = [0, 0, 0]
y=(255,255,0)
#/////////////////////////solids flats 
black = [
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
z,z,z,z,z,z,z,z,
]
yellow = [
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
]
green = [
w,w,w,w,w,w,w,w,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]
blue = [
w,w,w,w,w,w,w,w,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]
white = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,z,z,w,w,w,
w,w,w,z,z,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
]
red = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
]
#////////////////error
equis = [
z,r,r,r,r,r,r,z,
z,z,r,r,r,r,z,z,
r,z,z,r,r,z,z,r,
r,r,z,z,z,z,r,r,
r,r,r,z,z,r,r,r,
r,r,z,z,z,z,r,r,
r,z,z,r,r,z,z,r,
z,z,r,r,r,r,z,z,
]
#simple
COLIBSIMPLE=[red,white,blue,green,yellow,black]

#//////////////////////////simon says-show colors on startup-user moves to meet the colors
class Simon:
    def says(self):
        COL=0
        sense.set_pixels(random.choice(COLIBSIMPLE))
        time.sleep(.75)
        sense.set_pixels(random.choice(COLIBSIMPLE))
        time.sleep(.75)
        sense.set_pixels(random.choice(COLIBSIMPLE))
        time.sleep(.75)

        #user then moves to meet the colors
        sense.clear()
        while True:
            try:
                raw = sense.accel_raw
                x = raw["x"]
                y = raw["y"]
                z = raw["z"]
                #print (x,y,z)#save xyz data to typea#######
                
                #////////////////////////flats
                if (-0.06 < x < 0.06) and (-0.06 < y < 0.06) and (0.95 < z < 1.05):
                    sense.set_pixels(white)#flat up
                    COL='white'
                    
                elif (-0.025 < x < -0.020) and (-0.03 < y < -0.02) and (-0.95 > z > -1.05):
                    sense.set_pixels(black)#flat dwn
                    COL='black'
                    
                elif (-0.055 < x < 0.055) and (-.80 > y > -1.5) and (-0.2 < z < 0.2):
                    sense.set_pixels(green)#side1
                    COL='green'
    
                elif (-0.08 < x < 0.08) and (0.7 < y < 1.5) and (0.08 < z < 0.15):
                    sense.set_pixels(yellow)#side2
                    COL='yellow'

                elif (-0.05 < y < 0.05) and (-0.75 > x > -1.5)and (-0.006 < z < 0.015):
                    sense.set_pixels(blue)#vertical1
                    COL='blue'

                elif (1 > x > 0.9) and (-0.01 > y > -0.04) and (-0.66 < z < -0.025):
                    sense.set_pixels(red)#vertical2
                    COL='red'
                    
                else:
                    sense.set_pixels(equis)
                    COL='equis'

      
            except KeyboardInterrupt:
                sense.clear()
                break
        
S=Simon()
#S.Recall()
S.says()


