# Tal Rogozinski 
# 5/10/2022
# Whak-A-Mole Game!


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
l1backround=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\\fiveHoles.png')
l1background=p.transform.scale(l1backround,(WIDTH,HEIGHT ))
screen.blit(l1background,(0,0))
#Mole for the gmae
mole=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\molebigger.png')
deadmole=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\deadmolepng.png')
deadmole=p.transform.scale(mole,(90,100))
mole=p.transform.scale(mole,(90,100))
xm=0
ym=0
#coordinates for the holes
while check:
    screen.blit(l1background,(0,0))
    for case in p.event.get():
        if case.type==p.QUIT:
            check=False
        if case.type==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            xm=mouse_pos[0]
            ym=mouse_pos[1]
    print(xm,ym)
    
    #Create square fr menu
    #randomizing where the mole will pop up by ranodmizing the coordinates in the list
    randmole=random.choice(moles)
    if xm>randmole[0]:
        wack=True
    if wack:
        print("hit")
        screen.blit(l1background,(0,0))
        screen.blit(deadmole,randmole)
        p.display.update()
        p.time.delay(1000)
    else:
        wack=False
        screen.blit(mole,randmole)

    
    #creating an inscribed rectangle that will be inside of teh mole which is usefull becuase I need it for when I click on the mole


    


    p.display.update()
    p.time.delay(1500)


#having my cursor become a hammer which I am learining how to do from a youtube video: https://www.youtube.com/watch?v=dYa69SXoo80 by pyh///////////////




    


