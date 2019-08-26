import sys
sys.path.append("/home/pi/Desktop/NAVI/WANDER_LUST")
import random
from random import randint
import time
from sense_hat import SenseHat
sense=SenseHat()
sense.set_rotation(90)
sense.clear()

blue=(0,0,255)
yellow=(255,255,0)
red = (255, 0, 0)
white=(255,255,255)
black=(0,0,0)
green = (0, 255, 0)
def fortune():
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
                sys.exit()
            else:
                sense.clear()
        except KeyboardInterrupt:
            sense.clear()
            break


fortune()
