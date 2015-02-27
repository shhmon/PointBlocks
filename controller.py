import pygame, sys, functions
from tileC import Tile
from characterC import *
from interaction import interaction, menu_interaction
from menuC import *

S_MENU = 1
S_GAME = 2
S_ESC = 3

pygame.init()
pygame.mixer.init()

class Controller():

	List = []

	def __init__(self, state = S_MENU):

		self.screen = pygame.display.set_mode(Tile.screen_size)
		self.caption = 'PointBlocks v 1.0'
		self.state = state
		self.gamebackground = Tile.background
		self.menubackground = pygame.image.load("images/menu_bg.png")
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.button_size = (300, 50)

		Controller.List.append(self)



	def run(self):

		pygame.display.set_caption(self.caption)

		if self.state == S_MENU:
			
			play_button = Button('PLAY', Tile.screen_size[0] / 2 - self.button_size[0] / 2, 200, self.button_size[0], self.button_size[1], 'PLAY GAME')
			builder_button = Button('DEVELOP', Tile.screen_size[0] / 2 - self.button_size[0] / 2, 300, self.button_size[0], self.button_size[1], 'DEVELOP LEVEL')

			while self.state == S_MENU:
				self.state = functions.get_state()

				self.screen.blit(self.menubackground, (0,0))
				Button.draw_buttons(self.screen)
				menu_interaction(self.screen)

				pygame.display.flip()
				self.clock.tick(self.FPS)

		if self.state == S_GAME:

			Tile.create_tiles()

			bill = Character('Bill')
			bull = Character('Bull')

			functions.load_level(1)
			sound = pygame.mixer.Sound("audio/music.wav")
			sound.set_volume(.5)
			sound.play(-1)

			print Tile.MAP

			while self.state == S_GAME:
				self.state = functions.get_state()

				self.screen.blit(self.gamebackground, (0,0))
				Tile.draw_tiles(self.screen)
				Character.update_characters(bill, bull)
				Character.draw_characters(self.screen)

				interaction(self.screen, bill, bull)

				bill.movement()
				bull.movement()

				pygame.display.flip()
				self.clock.tick(self.FPS)


		if self.state == S_ESC:
			pass
