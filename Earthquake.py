import turtle
import pandas as pd
from math import *

#I used the irma.py to model the setup for this
#Latitude is y(east and west) #longitude is x(North and South)
#got the distance of lat in km from a website
def CaliSet():
    turtle.TurtleScreen._RUNNING=True #got this from https://stackoverflow.com/questions/46796846/python-turtle-terminator-error
    turtle.setup(1024,630) #pixels of window
    wn = turtle.Screen()
    wn.title('Cali Baby')
    wn.setworldcoordinates(-133.56926,30.85874,-108.94300,42.91534) #got these coordinates from google maps
    midpoint_x = (-133.56926+-108.94300)/2
    midpoint_y = (30.8587+42.91534)/2
    #1,340.57 kilometers North to South got using a site 

    map = 'PythonFinal/Cali2.gif'
    wn.register_shape(map)
    jimmy = turtle.Turtle()
    jimmy.shape(map)
    jimmy.up()
    jimmy.speed(0)
    jimmy.goto(midpoint_x,midpoint_y)

    bob = turtle.Turtle()  
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    return bob,krista,emily,wn #,map_bg_img



def CaribbeanSet():
    turtle.TurtleScreen._RUNNING=True
    turtle.setup(1024,509) #pixels of window
    
    wn = turtle.Screen()
    wn.title('Caribean')
    wn.setworldcoordinates(-94.21823,7.24111,-59.00667,24.04272) #got from google maps
    #(7.24111,-94.21823),(24.04272,-59.00667)
    midpoint_x = (-94.21823+-59.00667)/2
    midpoint_y = (7.24111+24.04272)/2

    map = 'PythonFinal/Caribbean.gif'
    wn.register_shape(map)
    jimmy = turtle.Turtle()
    jimmy.shape(map)
    jimmy.up()
    jimmy.speed(0)
    jimmy.goto(midpoint_x,midpoint_y)

    bob = turtle.Turtle()
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    #1,868.16 kilometers
    return bob,krista,emily,wn #,map_bg_img


def SEAsiaSet(): #good
    turtle.TurtleScreen._RUNNING=True
    turtle.setup(1029,492) #pixels of window
    
    wn = turtle.Screen()
    wn.title('South East Asia')
    wn.setworldcoordinates(94.94849,-10.97059,149.53941,14.96693) #got from google maps
    #(-10.97059,94.94849),(14.96693,149.53941) 
    midpoint_x = (94.94849+149.53941)/2
    midpoint_y = (-10.97059+14.96693)/2

    map = 'PythonFinal/SouthEastAsia.gif'
    wn.register_shape(map)
    jimmy = turtle.Turtle()
    jimmy.shape(map)
    jimmy.up()
    jimmy.speed(0)
    jimmy.goto(midpoint_x,midpoint_y)

    bob = turtle.Turtle()
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    #2,883.98 kilometers from North to South
    return bob,krista,emily,wn #,map_bg_img  

def AsiaSet():
    turtle.TurtleScreen._RUNNING=True
    turtle.setup(1024,442) #pixels of window
    wn = turtle.Screen()
    wn.title('Asia')
    x1 = 23.72260
    y1 = 10.56143
    x2 = 135.17298
    y2 = 50.49969
    wn.setworldcoordinates(x1,y1,x2,y2) #got these coordinates from google maps
    midpoint_x = (x1+x2)/2
    midpoint_y = (y1+y2)/2
    #4,440.72 kilometers North to South

    map = 'PythonFinal/Asia.gif'
    wn.register_shape(map)
    jimmy = turtle.Turtle()
    jimmy.shape(map)
    jimmy.up()
    jimmy.speed(0)
    jimmy.goto(midpoint_x,midpoint_y)

    bob = turtle.Turtle()  
    krista = turtle.Turtle()
    emily = turtle.Turtle()
    return bob,krista,emily,wn



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
    NS_dist = 1340.57
    Lat_dist = 42.91534-30.85874
    return (km*Lat_dist)/NS_dist

def distanceCaribbean(km):
    NS_dist = 1868.16
    Lat_dist = 24.04272-7.24111
    return (km*Lat_dist)/NS_dist

def distanceAsia(km):
    NS_dist = 4440.72
    Lat_dist = 50.49969-10.56143
    return (km*Lat_dist)/NS_dist


def perimeter(radius):
    return 2*pi*radius


def CaliGo(index_num):
    df_all = pd.read_csv('PythonFinal/Earthquakes.csv')
    df = df_all.loc[df_all['Area']=='Cali']
    lst = df.iloc[index_num]
    bob,krista,emily,wn = CaliSet()
    bob.speed(0)
    bob.shape('arrow')
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob.stamp()
    bob.width(5)
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceCali(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    bob.ht()
    
    krista.speed(0)
    krista.shape('arrow')
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista.stamp()
    krista.width(5)
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceCali(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    krista.ht()
    
    emily.speed(0)
    emily.shape('arrow')
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily.stamp()
    emily.width(5)
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceCali(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    emily.ht()
    
    
    turtle.exitonclick()

def SEGO(index_num):
    df_all = pd.read_csv('PythonFinal/Earthquakes.csv')
    df = df_all.loc[df_all['Area']=='SEAsia']
    lst = df.iloc[index_num]
    bob,krista,emily,wn = SEAsiaSet()
    bob.speed(0)
    bob.shape('arrow')
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob.stamp()
    bob.width(5)
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceSe(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    bob.ht()
    
    krista.speed(0)
    krista.up()
    krista.shape('arrow')
    krista.goto(int(lst[6]),int(lst[7]))
    krista.stamp()
    krista.width(5)
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceSe(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    krista.ht()
    
    emily.speed(0)
    emily.up()
    emily.shape('arrow')
    emily.goto(int(lst[10]),int(lst[11]))
    emily.stamp()
    emily.width(5)
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceSe(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    emily.ht()
    
    turtle.exitonclick()


def CaribeanGo(index_num):
    df_all = pd.read_csv('PythonFinal/Earthquakes.csv')
    df = df_all.loc[df_all['Area']=='Caribbean']
    lst = df.iloc[index_num]
    bob,krista,emily,wn = CaribbeanSet()
    bob.speed(0)
    bob.shape('arrow')
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob.stamp()
    bob.width(5)
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceCaribbean(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    bob.ht()
    
    krista.speed(0)
    krista.shape('arrow')
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista.stamp()
    krista.width(5)
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceCaribbean(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    krista.ht()
    
    emily.speed(0)
    emily.shape('arrow')
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily.stamp()
    emily.width(5)
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceCaribbean(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    emily.ht()
    
    turtle.exitonclick()

def AsiaGo(index_num):
    df_all = pd.read_csv('PythonFinal/Earthquakes.csv')
    df = df_all.loc[df_all['Area']=='Asia']
    lst = df.iloc[index_num]
    bob,krista,emily,wn = AsiaSet()
    bob.speed(0)
    bob.shape('arrow')
    bob.up()
    bob.goto(int(lst[2]),int(lst[3]))
    bob.stamp()
    bob.width(5)
    bob_waves = distance(lst[4],lst[5])
    bob_dis = distanceAsia(bob_waves)
    bob.goto(int(lst[2]),int(lst[3])-bob_dis)
    bob.setheading(0)
    bob.down()
    circ_bob = perimeter(bob_dis)
    for _ in range(100):
        bob.fd(circ_bob/100)
        bob.left(360/100)
    bob.ht()
    
    krista.speed(0)
    krista.shape('arrow')
    krista.up()
    krista.goto(int(lst[6]),int(lst[7]))
    krista.stamp()
    krista.width(5)
    krista_waves = distance(lst[8],lst[9])
    krista_dis = distanceAsia(krista_waves)
    krista.goto(int(lst[6]),int(lst[7])-krista_dis)
    krista.setheading(0)
    krista.down()
    circ_krista = perimeter(krista_dis)
    for _ in range(100):
        krista.fd(circ_krista/100)
        krista.left(360/100)
    krista.ht()
    
    emily.speed(0)
    emily.shape('arrow')
    emily.up()
    emily.goto(int(lst[10]),int(lst[11]))
    emily.stamp()
    emily.width(5)
    emily_waves = distance(lst[12],lst[13])
    emily_dis = distanceAsia(emily_waves)
    emily.goto(int(lst[10]),int(lst[11])-emily_dis)
    emily.setheading(0)
    emily.down()
    circ_emily = perimeter(emily_dis)
    for _ in range(100):
        emily.fd(circ_emily/100)
        emily.left(360/100)
    emily.ht()
    
    
    turtle.exitonclick()


def info():
    print('''    The process of locating Earthquakes is a rather interesting process called Triangulation.
    To start, you need 3 siesmic stations. From that, you then find two parts in the siesmograph reading.
    1. At what time the P waves start arriving. These are less powerful waves.
    2. At what time the S waves start arriving. Theses are more powerful waves. The highest S also tells the magnitude.
    From there, you then find the difference in arriving times. You can then use this to distance from the epicenter.
    Now, circles can be drawn from the siesmic stations with that distance as the radius.
    Where the 3 circles around the siesmic stations meet, that is where the epicenter is.

    ### Enter 0 to return to main number/99 to exit ###''')

def myInfo():
    print('''    How I am doing this:
    I am using the concept of Triangulation from the info.
    I choose areas that have a larger amount of Earthquakes (Asia, Southeast Asia, California, Caribbean).
    Finding earthquakes using the United States Geological Survey and Waveforms from Wilber 3, I got the data I needed.
    Using the data, I get the time in seconds after an earthquake that the P and S waves arrived at 3 stations.
    I also got the longitude and latitude of the 3 stations.
    Frome this, I convert the difference in time to a distance in kilometers (difference multiplied by 9.75).
    This isn't perfect, I got it from a lab in my Geology class.
    Using this distance, I then convert this to latitude for my map [(distance*difference in lat on map)/actual distance].
    I then go south of a seismic station by this much, set the turtle to face east.
    Then make a circle with the distance as the radius.
    Where the circles meet, or close to hit, there was an Earthquake there.

    ### Enter 0 to return to main number/99 to exit ###''')

def Downfalls():
    print('''    Some errors with my system:
    1. It works best for Earthquakes at a lower depth, since more depth effect wave speeds.
    2. Because of some of my set for turtles, the circles are ovals.
    3. It just isn't perfect, but it pretty close on a lot of Earthquakes.

    ### Enter 0 to return to main number/99 to exit ###''')

def menu():
    print('''    What would you like to explore:
    1. Information on how Earthquake Epicenters are located.
    2. More information on how I using Triangulation in my code.
    3. See some errors with my program.
    4. See Triangulation used in California.
    5. See Triangulaiton used in The Caribbean (not the strongest one).
    6. See Triangulation used in Southeast Asia (Indonesia and Malaysia).
    7. See Triangulation used in Asia (Turkey to China).

    Exit [99]''')

def CaliMenu():
    print('''    Earthquakes in California: 
    1. An Earthquake on 4/25/23 in between San Jose and Los Angeles.
    2. An Earthquake on 4/26/23 by San Jose. 
    3. A 2.5 Magnitude Earthquake on 4/27/23 in Northern California.
    4. A 3.2 Magnitued Earthquake on 4/27/23 Northeast of San Diego.

    Return to Main Menu [0]
    Exit [99]
    ### Wait for the turtles to finish, click the screen to close, then come back to the terminal ###''')

def CaribbeanMenu():
    print('''    Earthquakes in the Caribbean:
    1. Earthquake on 4/25/23 north of San Jaun, Puerto Rico.
    2. Earthquake on 4/26/23 southwest of Puerto Rico.
    3. A 2.8 Magnitude Earthquake on 4/27/23 south of Puerto Rico.

    Return to Main Menu [0]
    Exit [99]
    ### Wait for the turtles to finish, click the screen to close, then come back to the terminal ###''')

def SEasiaMenu():
    print('''    Earthquakes in Southeast Asia:
    1. A 7.1 Magnitude Earthquake by Indonesia on 4/24/23.
    2. A 4.7 Magnitude Earthquake in Papua New Guinea on 4/27/23.
    3. A 5.1 Magnitude Earthquake by Indonesia on 4/27/23.
    4. A 4.6 Magnitude Earthquake in Southern Indonesia on 4/27/23.

    Return to Main Menu [0]
    Exit [99]
    ### Wait for the turtles to finish, click the screen to close, then come back to the terminal ###''')

def AsiaMenu():
    print('''    Earthquakes in Asia:
    1. A 4.4 Magnitude Earthquake in China on 4/27/23.
    2. A 4.9 Magnitude Earthquake in Northern Iraq on 4/27/23.
    3. A 4.9 Magnitude Earthquake in Southern Iraq on 4/27/23.
    4. A 4.2 Magnitude Earthquake in Turkey on 4/27/23.
    5. A 4.1 Magnitude Earthquake in by Turkey on 4/28/23
    Return to Main Menu [0]
    Exit [99]
    ### Wait for the turtles to finish, click the screen to close, then come back to the terminal ### ''')


chose = 0
while chose != 99:
    print()
    menu()
    print()
    chose = int(input('What Would you like to do? ==>'))
    while chose not in [1,2,3,4,5,6,7,99]:
        print()
        print('Please enter either on of the following: [1,2,3,4,5,6,7,99]')
        chose = int(input('What Would you like to do? ==>'))
    if chose == 1:
        print()
        info()
        print()
        chose = int(input('Main Menu (0) or Exit (99) ==>'))
        while chose not in [0,99]:
            print()
            print('Please enter 0 or 99.')
            print()
            chose = int(input('Main Menu (0) or Exit (99) ==>'))
    if chose == 2:
        print()
        myInfo()
        print()
        chose = int(input('Main Menu (0) or Exit (99) ==>'))
        while chose not in [0,99]:
            print()
            print('Please enter 0 or 99.')
            print()
            chose = int(input('Main Menu (0) or Exit (99) ==>'))
    if chose == 3:
        print()
        Downfalls()
        print()
        chose = int(input('Main Menu (0) or Exit (99) ==>'))
        while chose not in [0,99]:
            print()
            print('Please enter 0 or 99.')
            print()
            chose = int(input('Main Menu (0) or Exit (99) ==>'))
    while chose == 4:
        print()
        CaliMenu()
        print()
        Eq = int(input('Which Earthquake ==>'))
        while Eq not in [0,1,2,3,4,99]:
            print()
            print('Please enter one of the following: [0,1,2,3,4,99]')
            print()
            Eq = int(input('Which Earthquake ==>'))
        if Eq == 99:
            chose = 99
            break
        go = Eq-1
        CaliGo(go)
        print()
        chose = int(input('California again [4] or Main Menu [0] ==>'))
        while chose not in [0,4]:
            print()
            print('Please input 0 or 4')
            print()
            chose = int(input('California again [4] or Main Menu [0] ==>'))
    while chose == 5:
        print()
        CaribbeanMenu()
        print()
        Eq = int(input('Which Earthquake ==>'))
        while Eq not in [0,1,2,3,99]:
            print()
            print('Please enter one of the following: [0,1,2,3,99]')
            print()
            Eq = int(input('Which Earthquake ==>'))
        if Eq == 99:
            chose = 99
            break
        go = Eq-1
        CaribeanGo(go)
        print()
        chose = int(input('Caribbean again [5] or Main Menu [0] ==>'))
        while chose not in [0,5]:
            print()
            print('Please input 0 or 5')
            print()
            chose = int(input('Caribbean again [5] or Main Menu [0] ==>'))
    while chose == 6:
        print()
        SEasiaMenu()
        print()
        Eq = int(input('Which Earthquake ==>'))
        while Eq not in [0,1,2,3,4,99]:
            print()
            print('Please enter one of the following: [0,1,2,3,4,99]')
            print()
            Eq = int(input('Which Earthquake ==>'))
        if Eq == 99:
            chose = 99
            break
        go = Eq-1
        SEGO(go)
        print()
        chose = int(input('Southeast Asia again [6] or Main Menu [0] ==>'))
        while chose not in [0,6]:
            print()
            print('Please input 0 or 6')
            print()
            chose = int(input('Southeast Asia again [6] or Main Menu [0] ==>'))
    while chose == 7:
        print()
        AsiaMenu()
        print()
        Eq = int(input('Which Earthquake ==>'))
        while Eq not in [0,1,2,3,4,5,99]:
            print()
            print('Please enter one of the following: [0,1,2,3,4,5,99]')
            print()
            Eq = int(input('Which Earthquake ==>'))
        if Eq == 99:
            chose = 99
            break
        go = Eq-1
        AsiaGo(go)
        print()
        chose = int(input('Asia again [7] or Main Menu [0] ==>'))
        while chose not in [0,7]:
            print()
            print('Please input 0 or 7')
            print()
            chose = int(input('Asia again [7] or Main Menu [0] ==>'))
    
    

