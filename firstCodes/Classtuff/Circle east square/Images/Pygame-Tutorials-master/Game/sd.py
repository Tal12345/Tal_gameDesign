

# My first step is going to be to import my necesarry libraries
# I will use p when creeating things on my screen and making my screen for my game
import pygame as p
# I will use this when I want my terminal to be cleared
import os 
# I will use this when I have the timer for each of my game levels
import time
# I will use this for my scoreboard
import datetime
# For randomizing the hole the mole will come out of 
import random
# This will clear my terminal when I run my code
os.system('cls')
#initialize p
p.init()

# name=input("What is your name? ")
#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=600
check=True
wack = False
#square variables
hitx = 20 
hity = 30 
hitwidth = 50 
hitlength = 90
hitbox=p.Rect(hitx,hity,hitwidth,hitlength)
moles=[(435,0),(170,80),(362,200),(158,390),(424,410)]
#create screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('Whak-A-Mole')

#Creating my backround for the game
l3background= p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\scene.gif')
l3background= p.transform.scale(l3background,(700,600))
screen.blit(l3background,(0,0))
mole=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\molebigger.png')
deadmole=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\deadmolepng.png')
hammer=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\hammer.png')
deadmole=p.transform.scale(deadmole,(90,100))
mole=p.transform.scale(mole,(90,100))
hammer=p.transform.scale(hammer,(20,20))
time_limit = 30
start_time=time.time()
xm=0
ym=0
count = 0
#coordinates for the holes
# making my hammer replace my cursor
# I used this to help me replace the cursor with my hammer
# def hamm():
#     #making the cursor invisible but it still has all of its functions
#     p.mouse.set_visible(False)
#     mouse_pos=p.mouse.get_pos()
#     x_mouse=mouse_pos[0]
#     y_mouse=mouse_pos[1]
#     # puting hammer in the x,y pos of the mouse
#     screen.blit(hammer,(x_mouse,y_mouse))
# Timer that counts down to thirty and ends the game
def timer():
    elapsed_time= time.time() - start_time
    moleTime=time_limit - int(elapsed_time)
    #print(moleTime)
    if elapsed_time > time_limit:
        print("game over")
        exit()
    return moleTime
while check:
    # For when you clcik out of the game
    for case in p.event.get():
        if case.type==p.QUIT:
            check=False
        if case.type==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            xm=mouse_pos[0]
            ym=mouse_pos[1]
    print(xm,ym)
    # count down
    max=timer()
    print(max)
    
    randmole=random.choice(moles)
    while (timer()-max ==0):
        
    # my background
        screen.blit(l3background,(0,0))
       
        # hamm()
        screen.blit(mole,randmole)
        p.display.update() 

    #Create square fr menu
    #randomizing where the mole will pop up by ranodmizing the coordinates in the list
    # mouse pos for when wacking
    if xm>randmole[0]:
        wack=True
        print(xm,randmole[0])
    # for when you click/wack on the mole
    if wack:
        print("hit")
        print(randmole)
        screen.blit(l3background,(0,0))
        screen.blit(deadmole,randmole)
        p.display.update()
        p.time.delay(500)
        wack=False
        xm=0
        count +=1
    