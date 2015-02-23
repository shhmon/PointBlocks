import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction

pygame.init()

screen = pygame.display.set_mode(Tile.screen_size)
pygame.display.set_caption('Point Blocks 0.01')

clock = pygame.time.Clock()
FPS = 60

Tile.load_level(1)
Tile.create_tiles()

bill = Bill(Tile.spawning_points[0][0], Tile.spawning_points[0][1])
bull = Bull(Tile.spawning_points[1][0], Tile.spawning_points[1][1])

while True:
    screen.fill([123,235,255])
    Tile.draw_tiles(screen)
    Character.update_characters(bill, bull)
    Character.draw_characters(screen)

    interaction(screen, bill)
    interaction(screen, bull)

    bill.movement()
    bull.movement() 

    #Tile.show_info(screen, bill, bull)

    pygame.display.flip()
    clock.tick(FPS)