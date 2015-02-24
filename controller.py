import pygame, sys, functions, develop
from tileC import Tile
from object_classes import *
from interaction import interaction

pygame.init()
pygame.mixer.init()


S_MENU = 1
S_GAME = 2
S_ESC = 3
S_DEVELOP = 100

FPS = 60

class Controller():

	def __init__(self, state = S_MENU):

		self.screen = pygame.display.set_mode(Tile.screen_size)
		self.state = state
		self.background = pygame.image.load("images/background.png")
		self.clock = pygame.time.Clock()

	def run(self):
		if self.state == S_MENU:
			pass

		elif self.state == S_GAME:

			functions.load_level(1)
			Tile.create_tiles()
			sound = pygame.mixer.Sound("audio/music.wav")
			sound.set_volume(.05)
			sound.play(-1)

			bill = Character('Bill')
			bull = Character('Bull')

			while True:
				self.screen.blit(self.background, (0,0))
				Tile.draw_tiles(self.screen)
				Character.update_characters(bill, bull)
				Character.draw_characters(self.screen)

				interaction(self.screen, bill, bull)

				bill.movement()
				bull.movement()

				#develop.show_info(self.screen)

				pygame.display.flip()
				self.clock.tick(FPS)


		elif self.state == S_ESC:
			pass

		elif self.state == S_DEVELOP:

			functions.load_level(100)
			Tile.create_tiles()

			while True:
				self.screen.fill((200,200,200))
				develop.draw_tiles(self.screen)
				develop.build_controls(self.screen)
				#develop.show_info(self.screen)

				pygame.display.flip()
				self.clock.tick(FPS)
