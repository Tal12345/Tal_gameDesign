#create diffrent types of fonts alll of teh time
#Tal Rogozinski
import os, pygame as p, time

p.init()
wind=p.display.set_mode((700,700))
p.display.set_caption('testing')


#creatignfont types of font diffrent ones

TITLE_FNT=p.font.SysFont('comicsans', 40)
MENU_FNT= p.font.SysFont('comicsans', 20)
INST_FNT=p.font.SysFont('comicsans', 20)
text=TITLE_FNT.render('Circle Eats Square', 1, (255, 130, 0))
wind.fill((255,255,255))
wind.blit(text, (40,50))

text1=INST_FNT.render ('In this game you must use your arrow keys to get the circle', 1, (0,255,0)) 
text2=INST_FNT.render('to touch the square and once the circle touches the square', 1, (0,255,0)) 
text3=INST_FNT.render('the cirlce will get bigger', 1, (0,255,0))
text4=INST_FNT.render('GET THE CIRCLE AS BIG AS POSSIBLE!!!',1, (0,255,0))



wind.blit(text1,(0,229))
wind.blit(text2,(0,200))
wind.blit(text3,(0,180))
wind.blit(text4,(0,160))
p.display.update()
p.time.delay(10000)