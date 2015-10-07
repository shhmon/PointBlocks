import pygame, random, functions
from tileC import Tile
from sprites import *


class Character(pygame.Rect):

    width, height = Tile.width, Tile.height
    List = []
    speedx = 0
    speedy = 0
    acceleration = 0.45

    #SUIT FOR TILE SIZE
    for i in range(2, 9):
        if Tile.width % i == 0 and Tile.height % i == 0:
            vel = i
            break

    #TRANSFORM SPRITES FOR ANY TILE SIZE

    bill_sprite_sad = pygame.transform.scale(bill_sprite_sad, (width, height))
    bull_sprite_sad = pygame.transform.scale(bull_sprite_sad, (width, height))
    bill_sprite_happy = pygame.transform.scale(bill_sprite_happy, (width, height))
    bull_sprite_happy = pygame.transform.scale(bull_sprite_happy, (width, height))

    def __init__(self, name):

        self.tx, self.ty = None, None
        self.x, self.y = 0, 0
        self.name = name
        self.unnatural = False
        self.sound = pygame.mixer.Sound("audio/swishandflick.wav")
        self.sound.set_volume(0.01)
        pygame.Rect.__init__(self, self.x, self.y, Character.width, Character.height)
        Character.List.append(self)

    def __str__(self):
        return str(self.get_number())

    def set_target(self, next_tile): #SETS A TARGET X & Y FOR THE MOVEMENT FUNCTION
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

            Tile.moves += 0.5

    def has_target(self): #RETURNS IF CHARACTER TARGET IS SET, FALSE OTHERWISE
        if self.tx == None and self.ty == None:
            return False
        else:
            return True

    def get_number(self):
        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def get_tile(self):
        return Tile.get_tile(self.get_number())

    @staticmethod
    def respawn():
        for character in Character.List:
            if character.name == 'Bill':
                character.x, character.y = Tile.get_tile(Tile.MAP['spawn'][0]).x, Tile.get_tile(Tile.MAP['spawn'][0]).y
            else:
                character.x, character.y = Tile.get_tile(Tile.MAP['spawn'][1]).x, Tile.get_tile(Tile.MAP['spawn'][1]).y

    @staticmethod
    def on_point(): #RETURNS TRUE IF BOTH CHARACTERS X & Y = meeting_point's X & Y (are on meeting_point)
        on = 0
        for character in Character.List:
            if character.x == Tile.get_tile(Tile.MAP['point']).x and character.y == Tile.get_tile(Tile.MAP['point']).y:
                on += 1
        if on == len(Character.List):
            return True

    @staticmethod
    def update_characters(bill, bull): #LOOKS FOR CHARACTERS FALLING IN HOLES OR STANDING ON MEETING POINT.

        try:
            for character in Character.List:
                if Tile.get_tile(character.get_number()).type == 'hole':
                    if Tile.get_tile(character.get_number()).x == character.x and Tile.get_tile(character.get_number()).y == character.y:
                        if not character.has_target():
                            functions.load_level(Tile.MAP['level'])

            if bill.x == Tile.get_tile(Tile.MAP['point']).x and bill.y == Tile.get_tile(Tile.MAP['point']).y and not Character.on_point():
                bill.status = 'happy'
                bull.status = 'sad'

            elif bull.x == Tile.get_tile(Tile.MAP['point']).x and bull.y == Tile.get_tile(Tile.MAP['point']).y and not Character.on_point():
                bull.status = 'happy'
                bill.status = 'sad'

            elif Character.on_point():
                bill.status = 'happy'
                bull.status = 'happy'
                functions.load_level(Tile.MAP['level'] + 1)

            else:
                bill.status = 'sad'
                bull.status = 'sad'

        except Exception, e:
            functions.load_level(Tile.MAP['level'])


    @staticmethod
    def draw_characters(screen): #CHANGES CHARACTER SPRITES ACCORDING TO THEIR STATUS (sad/happy)
        for character in Character.List:
            if character.status == 'sad':
                if character.name == 'Bill':
                    character.sprite = Character.bill_sprite_sad
                elif character.name == 'Bull':
                    character.sprite = Character.bull_sprite_sad

            elif character.status == 'happy':
                if character.name == 'Bill':
                    character.sprite = Character.bill_sprite_happy
                elif character.name == 'Bull':
                    character.sprite = Character.bull_sprite_happy

            screen.blit(character.sprite, (character.x, character.y))

    def movement(self): #MOVES CHARACTER ACCORDING TO VELOCITY ONE FRAME AT A TIME

        if self.tx != None and self.ty != None: #IF set_target DID ITS JOB

            X = self.x - self.tx
            Y = self.y - self.ty

            if self.unnatural == True: #UNNATURAL

                Character.speedx += X/100
                Character.speedy += Y/100

                print Character.speedx * 2

                if X < 0:
                    self.x += Character.speedx * 2
                elif X > 0:
                    self.x -= Character.speedx * 2
                if Y > 0:
                    self.y -= Character.speedy * 2
                elif Y < 0:
                    self.y += Character.speedy * 2

            else:

                if X < 0: #right
                    self.x += Character.vel
                elif X > 0: #left
                    self.x -= Character.vel

                if Y > 0: #down
                    self.y -= Character.vel
                elif Y < 0: #up
                    self.y += Character.vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None
                self.unnatural = False
