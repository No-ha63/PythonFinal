import turtle
import pandas as pd
import tkinter


def CaliSet():
    turtle.setup(1246,1462)
    
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(32.09969,-124.76537,42.18684,-114.00260)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Cali.png")

    canvas.create_image(-1356,-1452, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img

def test():
    bob,wn,map_bg_img = SEAsiaSet()
    bob.goto(-10.97059,94.94849,)
    bob.goto(14.96693,149.53941)
    turtle.exitonclick()


def CarribeanSet():
    turtle.setup(2492,1238)
    
    wn = turtle.Screen()
    wn.title('Caribean')
    wn.setworldcoordinates(7.24111,-94.21823,24.04272,-59.00667)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/Caribbean.png")

    canvas.create_image(-1356,-1452, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img


def SEAsiaSet(): #good
    turtle.setup(1029,492)
    
    wn = turtle.Screen()
    wn.title('South East Asia')
    wn.setworldcoordinates(-10.97059,94.94849,14.96693,149.53941)
    

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="PythonFinal/SouthEastAsia.png")

    canvas.create_image(-441,-1300, anchor = tkinter.NW, image=map_bg_img)

    bob = turtle.Turtle()

    return bob,wn,map_bg_img  




test()

