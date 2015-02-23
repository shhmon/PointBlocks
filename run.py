import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction

pygame.init()

sound = pygame.mixer.Sound("audio/music.wav")
sound.set_volume(.1)
sound.play(-1)


screen = pygame.display.set_mode(Tile.screen_size)
pygame.display.set_caption('Point Blocks 0.01')
background = pygame.image.load("images/background.png")

clock = pygame.time.Clock()
FPS = 60

Tile.load_level(1)
Tile.create_tiles()

bill = Bill(Tile.spawning_points[0][0], Tile.spawning_points[0][1])
bull = Bull(Tile.spawning_points[1][0], Tile.spawning_points[1][1])

while True:
    screen.blit(background, (0,0))
    Tile.draw_tiles(screen)
    Character.update_characters(bill, bull)
    Character.draw_characters(screen)

    interaction(screen, bill, bull)

    bill.movement()
    bull.movement() 

    #Tile.show_info(screen, bill, bull)

    pygame.display.flip()
    clock.tick(FPS)