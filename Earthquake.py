import turtle
import pandas as pd
import tkinter

#I used the irma.py to model the setup for this
#Latitude is y(east and west) #longitude is x(North and South)
def CaliSet():
    turtle.setup(873,1024) #pixels of window
    
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(-124.76537,32.09969,-114.00260,42.18684) #got these coordinates from google maps
    #1,121.59 kilometers North to South

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Cali.png")

    canvas.create_image(-1000,-1000, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()  

    return bob,wn,map_bg_img

def test():
    bob,wn,map_bg_img = CaliSet()
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
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Caribbean.png")

    canvas.create_image(-500,-1024, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()
     #1,868.16 kilometers
    return bob,wn,map_bg_img


def SEAsiaSet(): #good
    turtle.setup(1029,492) #pixels of window
    
    wn = turtle.Screen()
    wn.title('South East Asia')
    wn.setworldcoordinates(94.94849,-10.97059,149.53941,14.96693) #got from google maps
    #(-10.97059,94.94849),(14.96693,149.53941) 

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/SouthEastAsia.png")

    canvas.create_image(-438,-1300, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()
    #2,883.98 kilometers from North to South
    return bob,wn,map_bg_img  


def distance(swaves,pwaves):
    '''Gives the amount of km from the epicenter'''
    s_list = swaves.split(':') #got this data from online
    p_list = pwaves.split(':')
    s_sec = int(s_list[0])*60 + int(s_list[1])
    p_sec = int(p_list[0])*60 + int(p_list[1])
    return (p_sec-s_sec)*8.4 #might try 9.75 instead of 8.4 #found 8.4 online, 9.75 from the geo class

def distanceFormap(km): #prolly won't need
    '''Gives the amount of degrees in lat from epicenter
    for the map, going south the radius to start the circle'''
    return km/110.574 #got from stackflow

test()

