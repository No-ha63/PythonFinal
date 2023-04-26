import turtle
import pandas as pd
import tkinter as tk
from math import *

#I used the irma.py to model the setup for this
#Latitude is y(east and west) #longitude is x(North and South)
def CaliSet():
    turtle.setup(546,640) #pixels of window
    
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(-124.76537,32.09969,-114.00260,42.18684) #got these coordinates from google maps
    # 1,121.59 kilometers North to South

    canvas = wn.getcanvas()
    map_bg_img = tk.PhotoImage(file="PythonFinal/Cali.png")

    canvas.create_image(-873,-1024, anchor = tk.NW, image=map_bg_img)

    bob = turtle.Turtle()  
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    return bob,krista,emily,wn #,map_bg_img

def test():
    bob,krista,emily,wn = CaliSet()
    bob.goto(-124.76537,32.09969)
    bob.goto(-114.00260,42.18684)
    turtle.exitonclick()


def CarribeanSet():
    turtle.setup(1024,509) #pixels of window
    
    wn = turtle.Screen()
    wn.title('Caribean')
    wn.setworldcoordinates(-94.21823,7.24111,-59.00667,24.04272) #got from google maps
    #(7.24111,-94.21823),(24.04272,-59.00667)

    canvas = wn.getcanvas()
    map_bg_img = tk.PhotoImage(file="PythonFinal/Caribbean.png")

    canvas.create_image(-500,-1024, anchor = tk.NW, image=map_bg_img)

    bob = turtle.Turtle()
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    #1,868.16 kilometers
    return bob,krista,emily,wn #,map_bg_img


def SEAsiaSet(): #good
    turtle.setup(1029,492) #pixels of window
    
    wn = turtle.Screen()
    wn.title('South East Asia')
    wn.setworldcoordinates(94.94849,-10.97059,149.53941,14.96693) #got from google maps
    #(-10.97059,94.94849),(14.96693,149.53941) 

    canvas = wn.getcanvas()
    map_bg_img = tk.PhotoImage(file="PythonFinal/SouthEastAsia.png")

    canvas.create_image(-1300,-438, anchor = tk.NW, image=map_bg_img)

    bob = turtle.Turtle()
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    #2,883.98 kilometers from North to South
    return bob,krista,emily,wn #,map_bg_img  


def distance(pwaves,swaves):
    '''Gives the amount of km from the epicenter'''
    s_list = swaves.split(':') #got this data from online
    p_list = pwaves.split(':')
    s_sec = int(s_list[0])*60 + int(s_list[1])
    p_sec = int(p_list[0])*60 + int(p_list[1])
    return (s_sec-p_sec)*9.75 #might try 9.75 instead of 8.4 found 8.4 online, 9.75 from the geo class

def distanceSe(km):
    NS_dist = 2883.98
    lat_diff = 14.96693-(-10.97059)
    return (km*lat_diff)/NS_dist

def distanceCali(km):
    NS_dist = 1121.59
    Lat_dist = 42.18684-32.09969
    return (km*Lat_dist)/NS_dist

def distanceCarribean(km):
    NS_dist = 1868.16
    Lat_dist = 24.04272-7.24111
    return (km*Lat_dist)/NS_dist

def perimeter(radius):
    return 2*pi*radius


def CaliGo(index_num):
    df = pd.read_csv('PythonFinal/Earthquakes.csv')
    lst = df.iloc[index_num]
    bob,krista,emily,wn = CaliSet()
    bob.speed(0)
    bob.width(5)
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceCali(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    
    krista.speed(0)
    krista.width(5)
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceCali(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    
    emily.speed(0)
    emily.width(5)
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceCali(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    
    print('done')
    turtle.exitonclick()

def SEGO(index_num):
    df = pd.read_csv('PythonFinal/Earthquakes.csv')
    lst = df.iloc[index_num]
    bob,krista,emily,wn = SEAsiaSet()
    bob.speed(0)
    bob.width(5)
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceSe(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    
    krista.speed(0)
    krista.width(5)
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceSe(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    
    emily.speed(0)
    emily.width(5)
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceSe(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    print('done')
    turtle.exitonclick()

#SEGO(1)

def CaribeanGo(index_num):
    df = pd.read_csv('PythonFinal/Earthquakes.csv')
    lst = df.iloc[index_num]
    bob,krista,emily,wn = CarribeanSet()
    bob.speed(0)
    bob.width(5)
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceCarribean(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    
    krista.speed(0)
    krista.width(5)
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceCarribean(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    
    emily.speed(0)
    emily.width(5)
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceCarribean(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    print('done')
    turtle.exitonclick()

#CaliGo(0)
#SEGO(1)
#CaribeanGo(2)