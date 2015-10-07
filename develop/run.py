import pygame, develop, functions
from tileC import Tile
from object_classes import Character
from interaction import interaction

pygame.init()

screen = pygame.display.set_mode(Tile.screen_size)
pygame.display.set_caption("PointBlocks Level Builder v1.2")
clock = pygame.time.Clock()
FPS = 60

Tile.create_tiles()

bill = Character('Bill')
bull = Character('Bull')

while True:
	screen.fill((200,200,200))
	develop.draw_tiles(screen)
	develop.show_inter_window()
	#develop.show_info(screen)

	if develop.testing == True:

		try:
			Character.update_characters(bill, bull)
			Character.draw_characters(screen)

			interaction(screen, bill, bull)

			bill.movement()
			bull.movement()

		except Exception, e:
			print 'Seems like the map is not valid. Are you sure you have point block and spawning points set?'
			develop.testing = False

	else:

		develop.build_controls(screen)

	pygame.display.flip()
	clock.tick(FPS)