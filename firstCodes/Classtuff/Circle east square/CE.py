#Tal Rogozinski
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame

import os, random, time, pygame, math, datetime
from pickle import TRUE
from re import L, T
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
score=0
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
SIZE=False
BACK=False
SPRITE=False
ON_OFF=False


#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','Sound']
SizeList=['500x500', '800x800', '1000x1000']
BC_list=['aqua','']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
TITLE_FNT2=pygame.font.SysFont('comicsans', 40)
MENU_FNT2= pygame.font.SysFont('comicsans', 20)
INST_FNT2=pygame.font.SysFont('comicsans', 20)
RETURN= MENU_FNT.render('return',1,(cr_color))
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def returnFunction():
    global RETURN
    RETURN= MENU_FNT.render('Return',1,(cr_color))
    screen.blit(RETURN,(250,650))
def scoreBoard():
    myFile=open('firstCodes\Classtuff\cireate.txt', 'r')
    yi=150
    stuff=myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=200
    for i in range(N, -1, -1):
        print(stuff[i])
        text=INST_FNT2.render(stuff[i],1,(0,0,0))
        screen.blit(text,(20,j))
        j+=50
        pygame.display.update()
        pygame.time.delay(10)



def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
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
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    # pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            
            
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    screen.fill(background)
        #showing what the instructions will say
    tym=TITLE_FNT.render('Instructions',1,(0,0,255))
    text1=INST_FNT2.render ('In this game you must use your arrow keys to get the circle', 1, (255,85,0)) 
    text2=INST_FNT2.render('to touch the square and once the circle touches the square', 1, (255,85,0)) 
    text3=INST_FNT2.render('the cirlce will get bigger', 1, (255,85,0))
    text4=INST_FNT2.render('GET THE CIRCLE AS BIG AS POSSIBLE!!!',1, (255,85,0))



        #the size for each of the line of code of the instructions
    screen.blit(tym, (147, 20))
    screen.blit(text1,(10,230))
    screen.blit(text2,(10,260))
    screen.blit(text3,(10,290))
    screen.blit(text4,(10,320))
    pygame.display.update()
def keepScore(score):
    date=datetime.datetime.now()
    
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('firstCodes\Classtuff\cireate.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm>20 and xm<80) and (ym>250 and ym<290)):
        HEIGHT=500
        WIDTH=500
    if ((xm>20 and xm<80) and (ym>300 and ym<340)):
        HEIGHT=800
        WIDTH=800
    if ((xm>20 and xm<80) and (ym>350 and ym<390)):
        HEIGHT=1000
        WIDTH=1000
    screen=pygame.display.set_mode((WIDTH,HEIGHT))

    # randsize=random.choice(Sizes)
    # display=pygame.display.set_mode((randsize))
       
def playGame():


    move=5 #pixels
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30
    #circle variables
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    #inscribed Square:
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    square=pygame.Rect(xs,ys,wbox,hbox)
    global MAIN
    global LEV_I
    global score
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    sq_color=colors.get(randColor)
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True
    count=0
    while run:
        screen.fill(background)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                MAIN=True
                LEV_I=False
                
    
                
        if keys[pygame.K_ESCAPE]:
            run=False        
        if keys[pygame.K_a] and square.x >=move:
                square.x -= move #substract 5 from the x value
        if keys[pygame.K_d] and square.x <WIDTH-wbox:
            square.x += move  
        #Jumping part
        if not JUMP:
            if keys[pygame.K_w]:
                square.y -= move
            if keys[pygame.K_s]:
                square.y += move   
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount >=-MAX:
                square.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False

    #Finish circle
        if keys[pygame.K_LEFT] and xc >=rad+move:
            xc -= move #substract 5 from the x value
            insSquare.x -= move
        if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
            xc += move #substract 5 from the x value  
            insSquare.x += move
        if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
            yc += move #substract 5 from the x value
            insSquare.y += move
        if keys[pygame.K_UP] and yc >=rad+move:
            yc -= move #substract 5 from the x value  
            insSquare.y -= move
            
        checkCollide = square.colliderect(insSquare)
        if checkCollide:
            square.x=random.randint(wbox, WIDTH-wbox)
            square.y=random.randint(hbox, HEIGHT-hbox)
            score+=5   
            changeColor()
            sq_color=colors.get(randColor)
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
        if score >=25:
            run=False
            MAIN=True
            LEV_I=False



    

#sq_color=colors.get('navy')

#Making a rand c f the square
changeColor()
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
sjk=True
first=True
ss=True
xm=0
ym=0
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        #print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        returnFunction()
        first=False
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        returnFunction()
    if SIZE and sjk:
        print("Size")
        screen.fill(background)
        TitleMenu("SIZES")
        MainMenu(SizeList)
        changeSize(xm,ym)
        returnFunction()
        sjk=False
        if keys[pygame.K_ESCAPE]:
            SIZE=False
            SETT=True
            sjk=True


        


    if LEV_I:
        score=0
        screen.fill(background)
        playGame()
        print("I shld be t")
        LEV_I=False
        MAIN=True
        mouse_pos=(0,0)
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and ss:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        returnFunction()
        ss=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            ss=True

    if ((xm >20 and xm <80) and (ym >250 and ym <290))and MAIN :
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330)) and MAIN:
        MAIN=False
        SETT=True
        # if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        #     SETT=True
        #     SIZE=True
        #     MAIN=False
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN:
        MAIN=False
        LEV_I=True
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN:
        MAIN=False
        LEV_II=True
    if ((xm >20 and xm <80) and (ym >450 and ym <480))or LEV_III:
        MAIN=False
        LEV_III=True

      #250,650
    
    if ((xm >20 and xm <80) and (ym >500 and ym <530))or SCORE :
        MAIN=False
        SCORE=True
    if ((xm > 250 and ym > 600) and INST):
        MAIN=True
        INST=False
        first=True
    if ((xm > 250 and ym > 600) and SCORE):
        MAIN=True
        SCORE=False
        ss=True
    if ((xm > 250 and ym > 600) and SETT):
        MAIN=True
        SETT=False
    if ((xm >20 and xm <80) and (ym >250 and ym <290))and SETT :
        SETT=False
        SIZE=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330)) and SETT:
        MAIN=False
        BACK=True
        
        # if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        #     SETT=True
        #     SIZE=True
        #     MAIN=False
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and SETT:
        SPRITE=False
        SETT=False
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and SETT:
        SETT=False
        ON_OFF=True
    if ((xm > 250 and ym > 600) and SIZE):
        MAIN=True
        INST=False
        sjk=True
    
    # if (( xm > 200 and xm <300) and (ym > 650)):
    #     MAIN=True
    #     INST=False
    #     SETT=False 
        
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        
        keepScore(score)
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
#firstCodes\Classtuff\paperROck.py
#firstCodes\Classtuff
#C:\Users\RogozinskiT25\OneDrive - Greenhill School\Desktop\New folder\Tal_gameDesign\firstCodes\Classtuff
#C:\Users\RogozinskiT25\OneDrive - Greenhill School\Desktop\New folder\Tal_gameDesign\firstCodes\Classtuff\o.py