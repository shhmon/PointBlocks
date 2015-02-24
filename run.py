from controller import Controller

if __name__ == '__main__':
	c = Controller()
	c.run()

"""import pygame, sys, functions
from tileC import Tile
from object_classes import *
from interaction import interaction

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("audio/music.wav")
sound.set_volume(.01)
sound.play(-1)


screen = pygame.display.set_mode(Tile.screen_size)
pygame.display.set_caption('Point Blocks 0.1')
background = pygame.image.load("images/background.png")

clock = pygame.time.Clock()
FPS = 60

functions.load_level(1)
Tile.create_tiles()

bill = Character('Bill', Tile.MAP['spawn'][0][0], Tile.MAP['spawn'][0][1])
bull = Character('Bull', Tile.MAP['spawn'][1][0], Tile.MAP['spawn'][1][1])

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
    clock.tick(FPS)"""