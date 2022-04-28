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
# I will use this name to be saved into the game for scoring
name=input("What is your name? ")
#initialize p
p.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=600
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False

#List the list messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop

#create screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('Whak-A-Mole')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'black':[0,0,0]}
backcolor = ["Green", "Orange", "Black"]
#Get colors
background= colors.get('black')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=p.font.SysFont('Verdana', 60)
MENU_FNT=p.font.SysFont('Verdana', 30)
INST_FNT=p.font.SysFont('Verdana', 30)
#Create square fr menu

squareM=p.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (0,255,0))
    screen.fill((0,0,0))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        p.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    p.display.update()
    p.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False

def instr():

    print("in instr")
    myFile=open('firstCodes\Classtuff\Circle east square\instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()


    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        p.display.update()
        p.time.delay(50)
        yi+=50
    myFile.close()
def scoreBoard():
   print
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('firstCodes\Classtuff\cireate.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=p.display.set_mode((WIDTH,HEIGHT))
def levelone():
    p.display.bilt('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\word-image-8.webp')

#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()

#==============================================
#
#Beginning  main prram
sq_color=colors.get(randColor)
keys=p.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
xm=0 
ym=0
f_SEET=True
sc_size=False
set_first=True
c_first=True
ss=True
while check:
    for case in p.event.get():
        if case.type==p.QUIT:
            check=False
        if case.type ==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=p.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[p.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[p.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[p.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[p.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and ss:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        ss=False
    if SCORE:
        if keys[p.K_ESCAPE]:
            SCORE=False
            MAIN=True
            ss=True
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[p.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[p.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[p.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        p.display.update()
        p.time.delay(50)
        MAIN=False
        SCORE=False 
        p.time.delay(3000)
        check=False
    p.display.update()
    p.time.delay(10)

os.system('cls')
p.quit()

