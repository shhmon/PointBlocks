import pygame, random, functions
from tileC import Tile


class Character(pygame.Rect):

    width, height = 45, 45
    List = []
    vel = 3

    def __init__(self, name):

        self.tx, self.ty = None, None
        self.x, self.y = 0, 0
        self.name = name
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
    def respawn(bill, bull):
        bill.x, bill.y = Tile.get_tile(Tile.MAP['spawn'][0]).x, Tile.get_tile(Tile.MAP['spawn'][0]).y
        bull.x, bull.y = Tile.get_tile(Tile.MAP['spawn'][1]).x, Tile.get_tile(Tile.MAP['spawn'][1]).y

    @staticmethod
    def on_point(): #RETURNS TRUE IF BOTH CHARACTERS X & Y = meeting_point's X & Y (are on meeting_point)
        on = 0
        for character in Character.List:
            if character.x == Tile.get_tile(Tile.MAP['point']).x and character.y == Tile.get_tile(Tile.MAP['point']).y:
                on += 1
        if on == len(Character.List):
            return True

    @staticmethod
    def update_characters(bill, bull): #LOOKS FOR CHARACTERS FALLING IN HOLES OR STANDING ON MEETING POINT. IF loading_level IS TRUE, TELEPORTS CHARACTERS TO SPAWNING POINTS
        for character in Character.List:
            if Tile.get_tile(character.get_number()).type == 'hole':
                if Tile.get_tile(character.get_number()).x == character.x and Tile.get_tile(character.get_number()).y == character.y:
                    if not character.has_target():
                        Tile.freeze = True
                        functions.load_level(Tile.MAP['level'])

        if Tile.loading_level == True:
            Character.respawn(bill, bull)

        Tile.loading_level = False

        if bill.x == Tile.get_tile(Tile.MAP['point']).x and bill.y == Tile.get_tile(Tile.MAP['point']).y and not Character.on_point():
            bill.status = 'happy'
            bull.status = 'sad'

        elif bull.x == Tile.get_tile(Tile.MAP['point']).x and bull.y == Tile.get_tile(Tile.MAP['point']).y and not Character.on_point():
            bull.status = 'happy'
            bill.status = 'sad'

        elif Character.on_point():
            bill.status = 'happy'
            bull.status = 'happy'
            Tile.freeze = True
            functions.load_level(Tile.MAP['level'] + 1)

        else:
            bill.status = 'sad'
            bull.status = 'sad'


    @staticmethod
    def draw_characters(screen): #CHANGES CHARACTER SPRITES ACCORDING TO THEIR STATUS (sad/happy)
        for character in Character.List:
            if character.status == 'sad':
                if character.name == 'Bill':
                    character.sprite = pygame.image.load('images/bill.png')
                elif character.name == 'Bull':
                    character.sprite = pygame.image.load('images/bull.png')

            elif character.status == 'happy':
                if character.name == 'Bill':
                    character.sprite = pygame.image.load('images/bill_happy.png')
                elif character.name == 'Bull':
                    character.sprite = pygame.image.load('images/bull_happy.png')

            screen.blit(character.sprite, (character.x, character.y))

    def movement(self): #MOVES CHARACTER ACCORDING TO VELOCITY ONE FRAME AT A TIME

        if self.tx != None and self.ty != None: #IF set_target DID ITS JOB

            X = self.x - self.tx
            Y = self.y - self.ty

            if X < 0:
                self.x += Character.vel
            elif X > 0:
                self.x -= Character.vel

            if Y > 0:
                self.y -= Character.vel
            elif Y < 0:
                self.y += Character.vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None