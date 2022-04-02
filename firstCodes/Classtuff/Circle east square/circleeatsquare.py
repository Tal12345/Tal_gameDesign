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
import os, random, time, pygame, math
from turtle import update
#initialize pygame
pygame.init()


#Declare constants, variables, list, dictionaries, any object
#scree size

WIDTH=700
HEIGHT=700
check=True #for the while loop
move=5 #pixels
#square variables
xs=20
ys=20
wbox=30
hbox=30
wind=pygame.display.set_mode((WIDTH,HEIGHT))
xms=50
ymx=250
wb=30
hb=30
#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('pink')
randColor=''
cr_color=colors.get('white')

sq_color=colors.get('orange')
sqM_color=colors.get('orange')
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)


#creatignfont types of font diffrent ones
#definfing the title and instrucions

TITLE_FNT=pygame.font.SysFont('comicsans', 60)
MENU_FNT= pygame.font.SysFont('comicsans', 30)
INST_FNT=pygame.font.SysFont('comicsans', 30)
TITLE_FNT2=pygame.font.SysFont('comicsans', 40)
MENU_FNT2= pygame.font.SysFont('comicsans', 20)
INST_FNT2=pygame.font.SysFont('comicsans', 20)
#showing what the title will say
text=TITLE_FNT.render('Menu', 1, (255, 0, 0))
wind.fill((255,255,255))
texti=TITLE_FNT2.render('Circle Eats Square Game Instructions', 1, (255, 130, 0))
#get the width of our text so that we can cente rteh title
#x value should be equal tp the 1/2-width minue the width of the text/2
xt=WIDTH/2-text.get_width()/2

#list f messages
menuList=['Instructions','Settings', 'Exit','jofk','iasjbkf','jkaf','ksdj']
SettingList=['screensize','fnyt', 'backround', 'color', 'bifp', 'nvoano']
#create the function for the menu for each of the parts
txty=243
menuSquare=pygame.Rect(xms,ymx,wb,hb)
pygame.draw.rect(wind,sq_color, menuSquare)
def mainnmenu(Mlist):
    
   
    global txty
    txty=243
    wind=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('CIRCLE EATS SQUARE!!!!')
    for i in range(7):
        global menuSquare
        message=menuList[i]
        text=INST_FNT.render (message, 1, (0,255,0)) 
        wind.blit(text,(90,txty))
        pygame.draw.rect(wind,sq_color, menuSquare)
        menuSquare.y+=62
        txty +=62
    menuSquare=pygame.Rect(xms,ymx,wb,hb)
    pygame.draw.rect(wind,sqM_color, menuSquare)
    pygame.display.update()
    pygame.time.delay(200)
#the size for each of the line of code of the instructions

wind.blit(text, (xt,50))

def screenThree():
    wind=pygame.display.set_mode((700,700))
    pygame.display.set_caption('Instructions for Circle eats Square')
    #create first button for the isntrucions
     #showing what the title will say
    wind.fill((255,255,255))
    wind.blit(texti, (40,50))
    #showing what the instructions will say
    text1=INST_FNT2.render ('In this game you must use your arrow keys to get the circle', 1, (0,255,0)) 
    text2=INST_FNT2.render('to touch the square and once the circle touches the square', 1, (0,255,0)) 
    text3=INST_FNT2.render('the cirlce will get bigger', 1, (0,255,0))
    text4=INST_FNT2.render('GET THE CIRCLE AS BIG AS POSSIBLE!!!',1, (0,255,0))
    wind.blit(text1,(0,169))
    wind.blit(text2,(0,190))
    wind.blit(text3,(0,210))
    wind.blit(text4,(0,230))

    

#showing what the instructions will say

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

MAX=10
jumpCount=MAX
JUMP=False


while check:
    square.y= 250
    screen.fill(background)
    mainnmenu(menuList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    

    keys=pygame.key.get_pressed() 
# #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if (( mouse_pos[0] > 20 and mouse_pos[0] <60) and (mouse_pos[1] > 250 and mouse_pos[1] < 290)):
            screen.fill(background)
            screenThree('INSTRUCTIONS')

    
        #     if keys[pygame.K_a] and square.x >=move:
#         square.x -= move #substract 5 from the x value
#     if keys[pygame.K_d] and square.x <WIDTH-wbox:
#         square.x += move  

#     #Jumping part
#     if not JUMP:
#         if keys[pygame.K_w]:
#             square.y -= move
#         if keys[pygame.K_s]:
#             square.y += move   
#         if keys[pygame.K_SPACE]:
#             JUMP=True
#     else:
#         if jumpCount >=-MAX:
#             square.y -= jumpCount*abs(jumpCount)/2
#             jumpCount-=1
#         else:
#             jumpCount=MAX
#             JUMP=False



# #Finish circle
#     if keys[pygame.K_LEFT] and xc >=rad+move:
#         xc -= move #substract 5 from the x value
#         insSquare.x -= move
#     if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
#         xc += move #substract 5 from the x value  
#         insSquare.x += move
#     if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
#         yc += move #substract 5 from the x value
#         insSquare.y += move
#     if keys[pygame.K_UP] and yc >=rad+move:
#         yc -= move #substract 5 from the x value  
#         insSquare.y -= move
        
#     checkCollide = square.colliderect(insSquare)
#     if checkCollide:
#         square.x=random.randint(wbox, WIDTH-wbox)
#         square.y=random.randint(hbox, HEIGHT-hbox)   
#         changeColor()
#         sq_color=colors.get(randColor)
#         rad +=move
#         ibox=int(rad*math.sqrt(2))
#         startpoint = (int(xc-ibox/2),int(yc-ibox/2))
#         insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
        
    
#     pygame.draw.rect(screen, sq_color, square)
#     pygame.draw.rect(screen,cr_color, insSquare )
#     pygame.draw.circle(screen, cr_color, (xc,yc), rad)

    pygame.display.update()
    pygame.time.delay(10)

    mainnmenu
