import turtle
import pandas as pd
import tkinter


def CaliSet():
    turtle.setup(1246,1462)
    
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(32.09969,-124.76537,42.18684,-114.00260)

    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")


