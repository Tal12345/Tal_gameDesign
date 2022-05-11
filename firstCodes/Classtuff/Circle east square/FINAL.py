# Tal
# Final Game

#Importing necceary functions
import os, random, time, pygame, math, datetime
from re import L

# CLearing the terminal
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
score=0
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
#screen size
WIDTH=700
HEIGHT=600
check=True
wack = False
#square variables
hitx = 20 
hity = 30 
hitwidth = 50 
hitlength = 90
hitbox=pygame.Rect(hitx,hity,hitwidth,hitlength)
moles=[(435,0),(170,80),(362,200),(158,390),(424,410)]
moles2=[(120,70),(280,120),(490,110),(100,250),(330,300),(550,230),(200,440),(540,400)]
moles3=[(120,70),(310,70),(490,70),(90,170),(230,170),(380,170),(530,170),(110,340),(310,340),(500,340)]
l1backround=pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\\fiveHoles.png')
l1background=pygame.transform.scale(l1backround,(WIDTH,HEIGHT ))
l2background= pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\leveltwoback.png')
l2background= pygame.transform.scale(l2background,(WIDTH,HEIGHT))
l3background= pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\scene.gif')
l3background= pygame.transform.scale(l3background,(700,600))
mole=pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\molebigger.png')
deadmole=pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\deadmolepng.png')
hammer=pygame.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\hammer.png')
deadmole=pygame.transform.scale(deadmole,(90,100))
mole=pygame.transform.scale(mole,(90,100))
hammer=pygame.transform.scale(hammer,(20,20))
time_limit = 30
start_time=time.time()
xm=0
ym=0
count = 0
#Lists for game
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop
run=True
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Whak-A-Mole')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'black':[0,0,0]}
backcolor = ["Green", "Orange", "Black"]
#Get colors
background= colors.get('black')
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create different font types 
TITLE_FNT=pygame.font.SysFont('Fixedsys', 100)
MENU_FNT=pygame.font.SysFont('Fixedsys', 50)
INST_FNT=pygame.font.SysFont('Fixedsys', 40)
#Create square for menu
squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((13,2,30))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter and is for my menu
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(180,255,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
# This funcion replaces my cursor with a hammer I learned how to do this from this site, https://stackoverflow.com/questions/26451227/how-to-make-an-image-follow-the-mouse-cursor-in-pygame

def hamm():
    #making the cursor invisible but it still has all of its functions
    pygame.mouse.set_visible(False)
    mouse_pos=pygame.mouse.get_pos()
    x_mouse=mouse_pos[0]
    y_mouse=mouse_pos[1]
    # puting hammer in the x,y pos of the mouse
    screen.blit(hammer,(x_mouse,y_mouse))
# This function uses a file in which I wrote out my instructions for the game
def instr():

    print("in instr")
    myFile=open('firstCodes\Classtuff\Circle east square\instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()


    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, (255,255,244))
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()

def scoreBoard():
    # Socreborad in the game
    myFile=open('firstCodes\Classtuff\cireate.txt', 'r')
    yi=150
    stuff=myFile.readlines()
    myFile.close()
    stuff.sort(reverse=True)
    # showing the file for the scoreboard in the game
    for line in stuff:
        text=INST_FNT.render(line,1,(255,255,255))
        screen.blit(text,(300,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
        
        

def keepScore(score):
    # How I am keeping the score
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('firstCodes\Classtuff\cireate.txt','a') 
    myFile.write(scoreLine)
    myFile.close()

# This fucntions changes the screen size of the game 
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
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
# This functions creates a timer while the game is playing and once the timer is over teh game finishes
#https://www.youtube.com/watch?v=juSH7hmYUGA
def timer():
    elapsed_time= time.time() - start_time
    moleTime=time_limit - int(elapsed_time)
    #print(moleTime)
    if elapsed_time > time_limit:
        MAIN=True
    return moleTime
# This is my first level of the game
def playGame():
    global xm,ym
    global MAIN
    global LEV_I
    global wack
    run=True
    counter=0
    while run:
        # count down
        max=timer() 
        counter+=1
        while (timer()-max ==0):
            
        # my background
            screen.blit(l1background,(0,0))
        #replaces cursor with hamer
            # hamm()
            randmole=random.choice(moles)
            screen.blit(mole,randmole)
            pygame.display.update() 
 # For when you clcik out of the game
            for case in pygame.event.get():
                if case.type==pygame.QUIT:
                    run=False
                    break
                if case.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    xm=mouse_pos[0]
                    ym=mouse_pos[1]
                
                # count down
                max=timer()
                
            pygame.time.delay(800)
                #Create square fr menu
            #randomizing where the mole will pop up by ranodmizing the coordinates in the list
            # mouse pos for when wacking
            if xm>randmole[0]:
                wack=True
                print(xm,randmole[0])
            # for when you click/wack on the mole
            if wack:
                global score
                print("hit")
                print(randmole)
                screen.blit(l1background,(0,0))
                screen.blit(deadmole,randmole)
                pygame.display.update()
                pygame.time.delay(500)
                score+=1
                wack=False
                xm=0
        if counter > 10:
            keepScore(score)
            print("Out of timer while loop")
            MAIN=True
            LEV_I=False
            run=False
#Exact same as previous function however diffrent randmole positionas and backrounds
def playGame2():
    global xm,ym
    global MAIN
    global LEV_II
    global wack
    run2=True
    counter2=0
    while run2:
        # count down
        max=timer() 
        counter2+=1
        while (timer()-max ==0):
            
        # my background
            screen.blit(l2background,(0,0))
        #replaces cursor with hamer
            # hamm()
            randmole2=random.choice(moles2)
            screen.blit(mole,randmole2)
            pygame.display.update() 
 # For when you clcik out of the game
            for case in pygame.event.get():
                if case.type==pygame.QUIT:
                    run2=False
                    break
                if case.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    xm=mouse_pos[0]
                    ym=mouse_pos[1]
                
                # count down
                max=timer()
                
            pygame.time.delay(600)
                #Create square fr menu
            #randomizing where the mole will pop up by ranodmizing the coordinates in the list
            # mouse pos for when wacking
            if xm>randmole2[0]:
                wack=True
                print(xm,randmole2[0])
            # for when you click/wack on the mole
            if wack:
                global score
                print("hit")
                print(randmole2)
                screen.blit(l2background,(0,0))
                screen.blit(deadmole,randmole2)
                pygame.display.update()
                pygame.time.delay(500)
                score+=1
                wack=False
                xm=0
        if counter2 > 10:
            keepScore(score)
            print("Out of timer while loop")
            MAIN=True
            LEV_II=False
            run2=False

##Exact same as previous function however diffrent randmole positionas and backrounds
def playGame3():
    global xm,ym
    global MAIN
    global LEV_III
    global wack
    run3=True
    counter3=0
    while run3:
        # count down
        max=timer() 
        counter3+=1
        while (timer()-max ==0):
            
        # my background
            screen.blit(l3background,(0,0))
        #replaces cursor with hamer
            # hamm()
            randmole3=random.choice(moles3)
            screen.blit(mole,randmole3)
            pygame.display.update() 
 # For when you clcik out of the game
            for case in pygame.event.get():
                if case.type==pygame.QUIT:
                    run3=False
                    break
                if case.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    xm=mouse_pos[0]
                    ym=mouse_pos[1]
                
                # count down
                max=timer()
                
            pygame.time.delay(400)
                #Create square fr menu
            #randomizing where the mole will pop up by ranodmizing the coordinates in the list
            # mouse pos for when wacking
            if xm>randmole3[0]:
                wack=True
                print(xm,randmole3[0])
            # for when you click/wack on the mole
            if wack:
                global score
                print("hit")
                print(randmole3)
                screen.blit(l3background,(0,0))
                screen.blit(deadmole,randmole3)
                pygame.display.update()
                pygame.time.delay(500)
                score+=1
                wack=False
                xm=0
        if counter3 > 10:
            keepScore(score)
            print("Out of timer while loop")
            MAIN=True
            LEV_III=False
            run3=False



#==============================================
#
#Beginning  main prram
keys=pygame.key.get_pressed()
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
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    # Recalling MAIN as Menu so sofourth
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
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        playGame2()
        hamm()
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        playGame3()
        hamm()
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and ss:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        ss=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            ss=True
    #WHat happens if you lcick on these mouse poisitions while in the menu
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
    # What haapens if you click on this pos in the settings
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[pygame.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        # keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)

os.system('cls')
pygame.quit()