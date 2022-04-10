import pygame as p

p.init()

p.display.set_caption("Level Two")


walkRight = [p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\L9.png')]

bg=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\\bg.jpg')
man=p.image.load('firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\standing.png')

clock=p.time.Clock()
x=50
y=425
height=64
width=64
vel=5
Left=False
Right=False
walkCount=0

def Drawgame():
    global walkCount
    win.blit