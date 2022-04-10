
import os, time, random,math
from re import L
import pygame as p
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE
#initialize pygame
p.init()
#variables, constants, and objects
screen=p.display.set_mode((500,500))
# This goes outside the while loop, near the top of the program
walkRight = [p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L9.png')]
bg=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\\bg.jpg')
char=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\standing.png')
x=50
y=425
height=64
width=64
vel=5
# xc=random.randint(50, WIDTH-50)
# yc=random.randint(50,HEIGHT-50)
hbox=20  #height if rect
wbox=20
Left=False
Right=False
walkCount=0
  #width of rect
# rad=10    #radius of the circle
#inscribe square
# ibox=rad*math.sqrt(2)
# xi= xc-ibox/2
# yi= yc-ibox/2
# inscSq=p.Rect(xi,yi, ibox,ibox)

manX=0
manY=500-64
check=True
manSquare=p.Rect(manX,manY,64,64)
boulder = p.Rect(230,270,180,345) 
square=p.Rect(x,y,wbox,hbox)

JUMP=False
#create screen
screen=p.display.set_mode((500,500))

#define colors Dictionary dictio={key: values}
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229]}
#calling values from a dictionaty get('key')
background=colors.get('white')
cr_color=colors.get('mag')
#Create a sqaure rand color 
#sq_color=colors.get('aqua')
blColor=colors.get('aqua')
randColor=''
# def changeClr():
#     print(background)
#     global randColor
#     colorCheck=True
#     while colorCheck:
#         randColor=random.choice(list(colors))
#         print("rand Clr = ", randColor)
#         if colors.get(randColor)  == background:
#             print("backgrnd = randclr")
#             randColor=random.choice(list(colors))
#         else:
#             colorCheck=False
# changeClr()
# sq_color=colors.get(randColor)    
def changeGameWIndow():
    global  walkCount
    screen.blit(bg,(0,0))
    if walkCount + 1 >= 27:
        walkCount= 0
    if Left:
        screen.blit(walkLeft[walkCount//3],(x,y))
        walkCount+= 1

    elif Right:
        screen.blit(walkRight[walkCount//3],(x,y))
        walkCount+= 1
    else:
        screen.blit(char,(x,y))
    p.display.update


p.display.set_caption("Circle eats Square")
jumpCount=7
COUNT=7
impact=False
while check:
    move=10
    crash=boulder.colliderect(manSquare)
    if crash:
        impact = True
    else:
        impact=False

    for case in p.event.get():
        if case.type == p.QUIT:
            check=False
    keys=p.key.get_pressed() # this is a list
    print(impact)
    if case.type==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
    #Square Moves
    if keys[p.K_a] and manX>=move:
        square.x -= move
        # if not impact:
        manX -= move
        manSquare.x -= move
    if keys[p.K_d] and manX<500-wbox:
        square.x += move
        if not impact:
            manX += move
            manSquare.x += move
    if keys[p.K_LEFT] and x > vel:
        x-=vel
        Left=True
        Right=False
    elif keys[p.K_LEFT] and x < 500 - width - vel:
        x+=vel
        Right=True
        Left=False
    else:
        Right=False
        Left=False
        walkCount= 0

    #JUMP CODE
    if not JUMP:
        if keys[p.K_s]:
            square.y += move
            if not impact:
                manY += move
                manSquare.y += move
        if keys[p.K_w]:
            square.y -= move
            if not impact:
                manY -= move
                manSquare.y -= move
        if keys[p.K_SPACE]:
            JUMP=True
    else:
        if jumpCount >= -COUNT:
            square.y -= jumpCount*abs(jumpCount)/2
            manY -= jumpCount*abs(jumpCount)/2
            manSquare.y -= jumpCount*abs(jumpCount)/2
            jumpCount -=1
        else:
            jumpCount=COUNT
            JUMP=False
    changeGameWIndow()

    # #circle moves
    # if keys[p.K_LEFT] and xc > move:
    #     xc -= move
    #     inscSq.x -= move
    # if keys[p.K_RIGHT] and xc <WIDTH-(rad+move):
    #     xc += move
    #     inscSq.x += move
    # if keys[p.K_DOWN] and yc <HEIGHT-(rad+move):
    #     yc += move
    #     inscSq.y += move
    # if keys[p.K_UP] and yc > move:
    #     yc -= move
    #     inscSq.y -= move

   # choque=square.collidepoint((xc,yc))
    # choque=square.colliderect(inscSq )
    # if choque:
        # square.x=random.randint(50, WIDTH-50)
        # square.y=random.randint(50,HEIGHT-50)
        # changeClr()
        # sq_color=colors.get(randColor)    

        # rad +=move
        # ibox=rad*math.sqrt(2)
        # xi= xc-ibox/2
        # yi= yc-ibox/2
        # inscSq=p.Rect(xi,yi, ibox,ibox)
    #Check clide between the man and the bulder
    
    

    p.draw.rect(screen,1,manSquare)
    p.draw.rect(screen,blColor, boulder)
    screen.fill(background)
    screen.blit(bg,(0,0))

    screen.blit(char,(manX,manY))
    p.draw.rect(screen,(255,0,0),square)
    # p.draw.rect(screen,cr_color,inscSq)
    # p.draw.circle(screen,cr_color,(xc,yc), rad )
    p.display.update()
    p.time.delay(30)