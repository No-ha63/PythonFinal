import turtle
import pandas as pd
import tkinter


def CaliSet():
    turtle.setup(873,1024)
    
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(32.09969,-124.76537,42.18684,-114.00260)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Cali.png")

    canvas.create_image(-1000,-1000, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img

def test():
    bob,wn,map_bg_img = CaliSet()
    bob.goto(32.09969,-124.76537)
    bob.goto(42.18684,-114.00260)
    turtle.exitonclick()


def CarribeanSet():
    turtle.setup(1024,509)
    
    wn = turtle.Screen()
    wn.title('Caribean')
    wn.setworldcoordinates(7.24111,-94.21823,24.04272,-59.00667)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Caribbean.png")

    canvas.create_image(-500,-1024, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img


def SEAsiaSet(): #good
    turtle.setup(1029,492)
    
    wn = turtle.Screen()
    wn.title('South East Asia')
    wn.setworldcoordinates(-10.97059,94.94849,14.96693,149.53941)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/SouthEastAsia.png")

    canvas.create_image(-438,-1300, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img  


def distance(swaves,pwaves):
    s_list = swaves.split(':')
    p_list = pwaves.split(':')
    s_sec = int(s_list[0])*60 + int(s_list[1])
    p_sec = int(p_list[0])*60 + int(p_list[1])
    return (p_sec-s_sec)*8.4

def distanceFormap(km):
    return km/110.574

test()

