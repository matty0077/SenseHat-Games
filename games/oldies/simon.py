#import numpy as np
import time
import pandas as pd
from math import*
from sense_hat import SenseHat

sense = SenseHat()
r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255,255,255]
z = [0, 0, 0]
y=(255,255,0)
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
yellowimage = [
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
]

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
'''baba recaller-live color lvler'''
class Simon:
    #compares current data with classic data
    #and returns distance similarity
    #closer to zero the better
    def Recall(self):
        #knife path
        #boxing path

        #read live data
        g=pd.read_csv('typea.csv',usecols=['roll','pitch','yaw','accel_x','accel_y','accel_z','gyro_y','gyro_z'])
        sum1=g.sum()/len(g)#averages data in files
        print(sum1)

        #read perfect data
        g2=pd.read_csv('typeb.csv',usecols=['roll','pitch','yaw','accel_x','accel_y','accel_z','gyro_y','gyro_z'])
        sum2=g2.sum()/len(g2)#averages data in files
        print(sum2)

        #compares averages  aqrt==square root
        distance=sqrt(sum(pow(a-b,2) for a, b in zip(sum1,sum2)))
        #for i in g:
        print(distance)

#//////////////////////////simon says-show colors on startup-user moves to meet the colors
    def says(self,mode):
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
        
S=Simon()
#S.Recall()
S.says('ss')



#//////////////////////////////////////
'''def judge(self):                                                                         #header=0
    collection1=[]                                                              #index_col=0
    g=pd.read_csv('/home/pi/Desktop/NAVI/SPIRIT/WANDER_LUST/memory/Shingu/typea.csv',nrows=20,header=0,index_col=0)#, nrows=20)#)#false#0
    print(g)
    for i in g:
        #print(g)
        collection1.append(g)#split(",")
    #print(collection1)

    collection2=[]
    s=pd.read_csv('/home/pi/Desktop/NAVI/SPIRIT/WANDER_LUST/memory/Shingu/typeb.csv',nrows=20,header=0,index_col=0)#skipinitialspace=True,,delim_whitespace=True)
    for i in s:
        collection2.append(s)
    #print(collection2)

    collection3=[]
    for i in collection1:
        for j in collection2:
            estimate=abs(i-j)
            #print(estimate)
            collection3.append(estimate)
            b=len(collection3)-1
            if b>=0:
                truf=abs(collection1[b]-collection2[b])
                if all(truf>90):
                    print('yes')
                b-=1
                print(truf)
                #print(list(collection3))
            else:
                print('nada')'''

'''for i in collection3:
    emp= all(i>90)
    return emp'''
#/////////////////////////////method 2
'''import csv
#while True:
reader1 = csv.reader(open('/home/pi/Desktop/NAVI/WANDER_LUST/memory/EEG/live/live.csv', 'rb'))#, delimiter=',', quotechar='"'))
row1 = reader1.next()
reader2 = csv.reader(open('/home/pi/Desktop/NAVI/WANDER_LUST/memory/EEG/natural/true.csv', 'rb'))#, delimiter=',', quotechar='"'))
row2 = reader2.next()
print(row1)
if (row1[0] == row2[0]) and (row1[2:] == row2[2:]):
    print( "eq")
else:
    print ("different")'''


#/////////////////////////////method3
'''import csv multiple columns

interesting_cols = [0, 2, 3, 4, 5]

with open("file1.csv", 'r') as file1,\
     open("file2.csv", 'r') as file2:

    reader1, reader2 = csv.reader(file1), csv.reader(file2)

    for line1, line2 in zip(reader1, reader2):
        equal = all(x == y
            for n, (x, y) in enumerate(zip(line1, line2))
            if n in interesting_cols
        )
        print(equal)'''
