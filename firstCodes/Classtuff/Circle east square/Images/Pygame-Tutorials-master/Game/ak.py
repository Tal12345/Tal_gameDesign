import pygame
from pygame.locals import MOUSEBUTTONDOWN
import pygame.freetype
import random
import time
import math

pygame.init()

# constants
width = 300
height = 350
z = 2
BURROW_RADIUS = width // 10
score = int(0)
clock = pygame.time.Clock()
turn_number = int(0)
game_condition_list = ["going on", "over"]
game_condition = int(0)
check = turn_number - score
# colours
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

# loading mole image
mole_image = pygame.image.load("firstCodes\Classtuff\Circle east square\Images\Pygame-Tutorials-master\Game\mole.jpg")
modified_image = pygame.transform.scale(mole_image, (40, 40))

# Adding text to screen
font = pygame.freetype.SysFont("Arial", 20)

# burrow and mole positions
burrow_x = -50
burrow_y = 50
count = int(0)
burrow_positions_list = []
mole_positions_list = []
while count != 9:
    count += 1
    burrow_x += 100
    if burrow_x == 350:
        burrow_x -= 300
        burrow_y += 100
    tuple1 = (burrow_x, burrow_y)
    tuple2 = (burrow_x - 20, burrow_y - 20)
    burrow_positions_list.append(tuple1)
    mole_positions_list.append(tuple2)

# setting up the display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack A Mole")


# creating burrows for the moles
def Burrows():
    circle_count = int(-1)
    while circle_count != len(burrow_positions_list) - 1:
        circle_count += 1
        pygame.draw.circle(display, black, burrow_positions_list[circle_count], BURROW_RADIUS)


def Moles():
    display.blit(modified_image, random.choice(mole_positions_list))
    time.sleep(z)


def twoPointDistance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    x_squared = (x2 - x1) * (x2 - x1)
    y_squared = (y2 - y1) * (y2 - y1)
    length = math.sqrt(x_squared + y_squared)
    return length


# running pygame until quit
run = True
while run:
    # speeding up mole blitting
    z -= 0.05
    if z < 0.7:
        z += 0.05
    display.fill(white)
    Burrows()
    Moles()
    clock.tick(60)
    turn_number += 1
    font.render_to(display, (10, 320), f"Score: {score}", black)
    try:
      font.render_to(display, (100, 320), f"Game condition: {game_condition_list[game_condition]}", black)
    except IndexError:
      Burrows()
      time.sleep(2)
      pygame.quit()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Loop through every burrow point, checking the distance
            for i, burrow_point in enumerate(burrow_positions_list):
                if twoPointDistance(pos, burrow_point) < BURROW_RADIUS:
                    # Burrow was clicked
                    score += 1
                    pygame.draw.circle(display, black, burrow_positions_list[i], BURROW_RADIUS)

                    if turn_number - score > 2:
                        game_condition += 1
pygame.quit()