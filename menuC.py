import pygame, functions, sys

class Button(pygame.Rect):

	List = []

	def __init__(self, action, x, y, width, height, text, textcolor=(0,0,0), color=(255,255,255)):

		self.text = text
		self.textcolor = textcolor
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.action = action
		self.color = color

		Button.List.append(self)

	@staticmethod
	def draw_buttons(screen):

		for button in Button.List:

			pygame.draw.rect(screen, button.color, (button.x, button.y, button.width, button.height))

			functions.text_to_screen(screen, button.text, button.x, button.y + 10, color=button.textcolor, size=25)