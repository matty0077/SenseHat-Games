import sys
sys.path.append("/home/pi/Desktop/NAVI/SPIRIT/WANDER_LUST/")
import random
from random import randint
import time
from sense_hat import SenseHat
sense=SenseHat()
sense.set_rotation(90)
sense.clear()
#simonsays
import pandas as pd
from math import*
r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255,255,255]
z = [0, 0, 0]
#y=(255,255,0)
bl=(0,0,0)

blackimage = [
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
bl,bl,bl,bl,bl,bl,bl,bl,
]
'''yellowimage = [
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
]'''

redimage = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
]

greenimage = [
w,w,w,w,w,w,w,w,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]

blueimage = [
w,w,w,w,w,w,w,w,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

whiteimage = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,z,z,w,w,w,
w,w,w,z,z,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
]
#maze
r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)
game_over=False

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,r,r,r],
        [r,b,r,b,r,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,g,b,b,r],
        [r,r,r,r,r,r,r,r]]
#dice
b = [0, 0, 0]
g = [0, 255, 0]
r = [255, 0, 0]

one = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

two = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,g,g,b,b,
b,b,b,b,g,g,b,b,
b,b,b,b,b,b,b,b,
]

three = [
g,g,b,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,g,g,
b,b,b,b,b,b,g,g,
]

four = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
]

five = [
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
]

six = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]
#
blue=(0,0,255)
yellow=(255,255,0)
red = (255, 0, 0)
white=(255,255,255)
black=(0,0,0)
green = (0, 255, 0)
x=1
y=1

class Gamer:
    def gentle_close(self): # A function to end the program gracefully
        #self.run=False
        sense.clear(255,0,0) # Turn on the LEDs red
        time.sleep(0.5) # Wait half a second
        sense.clear(0,0,0) # Turn all the LEDs off
        #self.Manual()
        import Saving_Grace
        #sys.exit() # Quit the program
        
    #magic 8ball
    def fortune(self):
        sense.show_message("Ask a question", scroll_speed=0.06)
        time.sleep(3)

        replies = ['Signs point to yes',
                'Without a doubt',
                'You may rely on it',
                'Do not count on it',
                'Looking good',
                'Cannot predict now',
                'It is decidedly so',
                'Outlook not so good'
                ]

        while True:
            try:
                x, y, z = sense.get_accelerometer_raw().values()

                x = abs(x)
                y = abs(y)
                z = abs(z)

                if x > 2 or y > 2 or z > 2 :
                    sense.show_message(random.choice(replies))
                    sense.clear()
                    import Saving_Grace
                    sys.exit()
                else:
                    sense.clear()
            except KeyboardInterrupt:
                sense.clear()
                break
#////////////////dice
    def roll_dice(self):
        r = random.randint(1,6)
        if r == 1:
            sense.set_pixels(one)
        elif r == 2:
            sense.set_pixels(two)
        elif r == 3:
            sense.set_pixels(three)
        elif r == 4:
            sense.set_pixels(four)
        elif r == 5:
            sense.set_pixels(five)
        elif r == 6:
            sense.set_pixels(six)
    def DICER(self):
        sense.show_message("Shake to roll!",scroll_speed=.04)
        while True:
            try:
                x, y, z = sense.get_accelerometer_raw().values()

                x = abs(x)
                y = abs(y)
                z = abs(z)

                if x > 1.4 or y > 1.4 or z > 1.4:
                    self.roll_dice()
                    time.sleep(4)
                    self.gentle_close()
            except KeyboardInterrupt:
                sense.clear()
                break
#///////////////////////////jokes
    def jokes(self):
# jokes from http://www.laughfactory.com/jokes/word-play-jokes
        jokes = [
            "What happens to a frog's car when it breaks down? It gets toad away",
            "Why was six scared of seven? Because seven eight nine",
            "What do you call a bear with no teeth? A gummy bear",
            "How do you count cows? With a cowculator",
            "How do astronomers organize a party? They planet",
            "Why does Humpty Dumpty love autumn? Because Humpty Dumpty had a great fall",
            "I went to the bank the other day and asked the banker to check my balance, so she pushed me!",
            "Can a kangaroo jump higher than the Empire State Building? Of course. The Empire State Building can't jump",
            "Did you hear about the kidnapping at school? It's okay. He woke up",
            "A man got hit in the head with a can of Coke, but he was alright because it was a soft drink",
        ]

        joke = random.choice(jokes)
        sense.show_message(joke)
        time.sleep(1)
        #self.gentle_close()
        import Saving_Grace
        #sys.exit()

#//////////////////////////////maze
    def move_marble(self,pitch,roll,x,y):
        new_x = x
        new_y = y
        if 10 < pitch < 170 and x != 0:
            new_x -= 1
        elif 350 > pitch > 170 and x != 7 :
            new_x += 1
        if 10 < roll < 170 and y != 7:
            new_y += 1
        elif 350 > roll > 170 and y != 0 :
            new_y -= 1
        x,y = self.check_wall(x,y,new_x,new_y)
        return x,y

    def check_wall(self,x,y,new_x,new_y):
        if maze[new_y][new_x] != r:
            return new_x, new_y
        elif maze[new_y][x] != r:
            return x, new_y
        elif maze[y][new_x] != r:
            return new_x, y
        else:
            return x,y

    def check_win(self,x,y):
        if maze[y][x] == g:
            game_over = True
            sense.show_message('You Win')
            #import Saving_Grace
            sys.exit()
    def maze(self):
        while not game_over:
            try:
                pitch = sense.get_orientation()['pitch']
                roll = sense.get_orientation()['roll']
                x,y = self.move_marble(pitch,roll,x,y)
                self.check_win(x,y)
                maze[y][x] = w
                sense.set_pixels(sum(maze,[]))
                sleep(0.01)
                maze[y][x] = b
            except KeyboardInterrupt:
                sense.clear()
                break

#/////////////////////////simon says
    def simon(self,mode):
        if mode=='ss':
            sense.set_pixels(redimage)
            time.sleep(.5)
            sense.set_pixels(blueimage)
            time.sleep(.5)
            sense.set_pixels(greenimage)
            time.sleep(.5)

        #user then moves to meet the colors
        sense.clear()
        sense.set_pixels(redimage)
        while True:
            try:
                raw = sense.accel_raw
                x = raw["x"]
                y = raw["y"]
                z = raw["z"]
                print (x,y,z)#save xyz data to typea#######
                
                if (-0.04 < x < 0.04) and (-0.04 < y < 0.04) and (0.98 < z < 1.02):
                    sense.set_pixels(whiteimage)
                elif (-0.04 < x < 0.04) and (-0.90 > y > -1.1):
                    sense.set_pixels(greenimage)
                elif (0.98 > x > -1.04) and (0.04 > y > 0):
                    sense.set_pixels(yellowimage)
                elif (0.98 > y > -1.04) and (0.04 > x > 0):
                    sense.set_pixels(blackimage)
                elif (-0.02 < y < 0.02) and (-0.90 > x > -1.1):
                    sense.set_pixels(blueimage)
                else:
                    sense.set_pixels(redimage)
            except KeyboardInterrupt:
                break


    
A=Gamer()
#G.DICER()
#G.fortune()
#A.jokes()
A.maze()
#G.simon()
