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
os.system('cls')
from pickle import TRUE
# name=input("What is your name?: ")
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
MAIN=TRUE
INST=False
SETT=False
LEV_I=False

#List f messages
MenuList=['Instructions','Settings', " Level 1","dasdas",'fdgdfg','asdasd','asdasd']
settingsList=['Screensize','Circle color', 'Speed','Highscore','Sound']
check=True #for the while loop
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
print(startpoint[0]-ibox,startpoint[1])
insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

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

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
TITLE_FNT2=pygame.font.SysFont('comicsans', 40)
MENU_FNT2= pygame.font.SysFont('comicsans', 20)
INST_FNT2=pygame.font.SysFont('comicsans', 20)

RETURN= MENU_FNT.render('return',1,(cr_color))
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,20))    

#Create First button


#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#This is a function uses a parameter
def returnFunction():
   
    settingsback = INST_FNT.render("Return",1,(158,33,37))   
    screen.blit(settingsback,(250,HEIGHT-100)) 

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
    if SETT:
        returnFunction()
    pygame.display.update()
    pygame.time.delay(10)
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

#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
sq_color=colors.get(randColor)

def returnFunction():
   
    settingsback = INST_FNT.render("Return",1,(158,33,37))   
    screen.blit(settingsback,(250,HEIGHT-100)) 

#This is a function uses a parameter
def SettingMenu(Slist):
    txty=243
    squareM.y=250
    for i in range(len(Slist)):
        message=Slist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50

def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    # scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')

    myFile=open('firstCodes\Classtuff\cireate.txt','a')
    # myFile.write(scoreLine)
    myFile.close()
MAX=10
jumpCount=MAX
JUMP=False
while check:
    
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(settingsList) 
        returnFunction()
       
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0] <70) and (mouse_pos[1] >250 and mouse_pos[1] <290)): 
            MAIN=False
            INST=True
            SETT=False
        if (( mouse_pos[0] > 200 and mouse_pos[0] <300) and (mouse_pos[1] > 650)):
            MAIN=True
            INST=False
            SETT=False
        if (( mouse_pos[0] > 20 and mouse_pos[0] <70) and (mouse_pos[1]> 300 and mouse_pos[1] <390)):
            MAIN=False
            INST=False
            SETT=True
        if (( mouse_pos[0] > 200 and mouse_pos[0] <300) and (mouse_pos[1] > HEIGHT-100)and SETT):
            MAIN=True
            INST=False
            SETT=False
        # if (( mouse_pos[0]>20 and mouse_pos[0]< 70) and (mouse_pos[1]> 300 and mouse_pos[1]< 490)):
        #     MAIN=False
        #     INST=False
        #     SETT=False
        #     LEV_I=True





    if INST:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        #showing what the instructions will say
        text1=INST_FNT2.render ('In this game you must use your arrow keys to get the circle', 1, (0,255,0)) 
        text2=INST_FNT2.render('to touch the square and once the circle touches the square', 1, (0,255,0)) 
        text3=INST_FNT2.render('the cirlce will get bigger', 1, (0,255,0))
        text4=INST_FNT2.render('GET THE CIRCLE AS BIG AS POSSIBLE!!!',1, (0,255,0))



        #the size for each of the line of code of the instructions
        screen.blit(text1,(0,230))
        screen.blit(text2,(0,260))
        screen.blit(text3,(0,290))
        screen.blit(text4,(0,320))
        screen.blit(RETURN,(250,650))
        pygame.display.update()


def playGame():
    keys=pygame.key.get_pressed()
    square.x=random.randint(wbox, WIDTH-wbox)
    
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
