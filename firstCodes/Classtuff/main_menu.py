#Tal Rogozinski
#3/23/2022
#making a menu for the circle eats menuSquare game
#creating functions for the menu


#what we wneed o crete the games
import os, pygame as p, time, random
#creating the actual screen
p.init()
#creating variables we will need for the menu
WIDTH=700
HEIGHT=700


#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
backgroundM= colors.get('pink')
randColor=''

sqM_color=colors.get('orange')
#make screen
wind=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('CIRCLE EATS menuSquare!!!!')


#creatignfont types of font diffrent ones
#definfing the title and instrucions

TITLE_FNT=p.font.SysFont('comicsans', 60)
MENU_FNT= p.font.SysFont('comicsans', 30)
INST_FNT=p.font.SysFont('comicsans', 30)

#showing what the title will say
text=TITLE_FNT.render('Menu', 1, (255, 0, 0))
wind.fill((255,255,255))
#get the width of our text so that we can cente rteh title
#x value should be equal tp the 1/2-width minue the width of the text/2
xt=WIDTH/2-text.get_width()/2



wind.blit(text, (xt,50))

#create first button for the isntrucions

#showing what the instructions will say







#create menuSquare for the menu
xms=50
ymx=250
wb=30
hb=30
menuSquare=p.Rect(xms,ymx,wb,hb)
p.draw.rect(wind,sqM_color, menuSquare)


#list f messages
menuList=['Instructions','Settings', 'Exit','jofk','iasjbkf','jkaf','ksdj']

#create the function for the menu for each of the parts
txty=243

for i in range(7):
    message=menuList[i]
    text=INST_FNT.render (message, 1, (0,255,0)) 
    wind.blit(text,(90,txty))
    p.draw.rect(wind,sqM_color, menuSquare)
    menuSquare.y+=62
    txty +=62
#the size for each of the line of code of the instructions

p.display.update()
p.time.delay(10000)
#02/23/22
#Ideas for setting 
# screen size
# background color
# circle color
# sound on/off
# create the main menu
# what we willl learn today
# how to be able to click on something in pygame
# also we will create return function for each part of our menu



