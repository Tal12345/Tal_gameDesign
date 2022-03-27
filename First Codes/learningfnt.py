#create diffrent types of fonts alll of teh time
#Tal Rogozinski
#what we wneed o crete the games
import os, pygame as p, time
#creating the actual screen
p.init()
wind=p.display.set_mode((700,700))
p.display.set_caption('Instructions for Circle eats Square')


#creatignfont types of font diffrent ones
#definfing the title and instrucions
TITLE_FNT2=p.font.SysFont('comicsans', 40)
MENU_FNT2= p.font.SysFont('comicsans', 20)
INST_FNT2=p.font.SysFont('comicsans', 20)
#showing what the title will say
text=TITLE_FNT2.render('Circle Eats Square Game Instructions', 1, (255, 130, 0))
wind.fill((255,255,255))
wind.blit(text, (40,50))
#showing what the instructions will say
text1=INST_FNT2.render ('In this game you must use your arrow keys to get the circle', 1, (0,255,0)) 
text2=INST_FNT2.render('to touch the square and once the circle touches the square', 1, (0,255,0)) 
text3=INST_FNT2.render('the cirlce will get bigger', 1, (0,255,0))
text4=INST_FNT2.render('GET THE CIRCLE AS BIG AS POSSIBLE!!!',1, (0,255,0))



#the size for each of the line of code of the instructions
wind.blit(text1,(0,169))
wind.blit(text2,(0,190))
wind.blit(text3,(0,210))
wind.blit(text4,(0,230))
p.display.update()
p.time.delay(10000000000000000000)
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



