import pygame, functions
from sprites import *

class Tile(pygame.Rect):

    #SCREEN & TILE SIZE PROPERTIES


    List = []
    aim_screen_size = (1000, 700)
    width, height = 45, 45 #maps made for 45, 45
    total_tiles = 1

    #SCREEN SIZE SUITS EVERY TILE SIZE

    screen_size = (int(aim_screen_size[0] / width) * width, int(aim_screen_size[1] / height) * height)
    H, V = 1, screen_size[0] / width

    #TRANSFORM SPRITES FOR ANY TILE SIZE

    background = pygame.transform.scale(background, (screen_size[0], screen_size[1]))

    solid_block = pygame.transform.scale(solid_block, (width, height))
    point_block = pygame.transform.scale(point_block, (width, height))
    hole_block = pygame.transform.scale(hole_block, (width, height))

    solid_block_edge = pygame.transform.scale(solid_block_edge, (width, height * 83/45))
    point_block_edge = pygame.transform.scale(point_block_edge, (width, height * 83/45))
    hole_block_edge = pygame.transform.scale(hole_block_edge, (width, height * 83/45))

    #LEVEL PROPERTIES

    MAP = {'level' : 0, 'solids' : [], 'holes' : [], 'point' : 0, 'spawn' : []} #MAP: level, valdis, holes, point, spawn
    moves = 0


    @staticmethod
    def create_tiles(): #SPLITS THE SCREEN INTO TILES AND GIVES THEM TYPES. (ONE TIME RUN)
        for y in range(0, Tile.screen_size[1], Tile.height):
            for x in range(0, Tile.screen_size[0], Tile.width):
                if Tile.total_tiles in Tile.MAP['solids']:
                    Tile(x, y, 'solid')
                elif Tile.total_tiles == Tile.MAP ['point']:
                    Tile(x, y, 'point')
                elif Tile.total_tiles in Tile.MAP['holes']:
                    Tile(x, y, 'hole')
                else:
                    Tile(x, y, 'empty')

        for tile in Tile.List:
            if tile.type == 'empty':
                tile.walkable = False
            else:
                tile.walkable = True

    @staticmethod
    def retype():
        for tile in Tile.List:
            tile.type = 'empty'
        for tile in Tile.List:
            if tile.number in Tile.MAP['solids']:
                tile.type = 'solid'
            elif tile.number == Tile.MAP ['point']:
                tile.type = 'point'
            elif tile.number in Tile.MAP['holes']:
                tile.type = 'hole'
            else:
                tile.type = 'empty'

        for tile in Tile.List:
            if tile.type == 'empty':
                tile.walkable = False
            else:
                tile.walkable = True

    @staticmethod
    def clear_map_dict():
        Tile.MAP = {'level' : 0, 'solids' : [], 'holes' : [], 'point' : 0, 'spawn' : []}

    def __init__(self, x, y, Type):

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

        Tile.List.append(self)


    @staticmethod
    def get_tile(number): #RETURNS A TILE OBJECT IF PASSED THE OBJECTS .number VARIABLE
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tiles(screen): #DRAWS TILES TO SCREEN ACCORDING TO TYPE (point/hole/solid/empty)
        for tile in Tile.List:
            if (tile.walkable):
                if tile.number < Tile.total_tiles - Tile.V:
                    tile_below = Tile.get_tile(tile.number + Tile.V)
                    if (tile_below.walkable):
                        if tile.type == 'point':
                            screen.blit(Tile.point_block, (tile))
                        elif tile.type == 'hole':
                            screen.blit(Tile.hole_block, (tile))
                        else:
                            screen.blit(Tile.solid_block, (tile))
                    else:
                        if tile.type == 'point':
                            screen.blit(Tile.point_block_edge, (tile))
                        elif tile.type == 'hole':
                            screen.blit(Tile.hole_block_edge, (tile))
                        else:
                            screen.blit(Tile.solid_block_edge, (tile))

        functions.text_to_screen(screen, 'Level: ' + str(Tile.MAP['level']), 20, 20, color = (0,0,0))

        if (Tile.moves + 1) % int(Tile.moves + 1) != 0:
                Tile.moves += 0.5

        functions.text_to_screen(screen, 'Moves: ' + str(int(Tile.moves + 0.5)), 20, 40, color = (0,0,0))

    def __str__(self):
        return str(self.number)
