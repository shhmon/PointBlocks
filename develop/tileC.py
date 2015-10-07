import pygame, functions

class Tile(pygame.Rect):

    List = []
    freeze = False
    screen_size = (990, 675)
    width, height = 45, 45
    total_tiles = 1
    H, V = 1, 22

    solid_block = pygame.image.load("images/solid_block.png")
    solid_block_edge = pygame.image.load("images/solid_block_edge.png")
    point_block = pygame.image.load("images/point_block.png")
    point_block_edge = pygame.image.load("images/point_block_edge.png")
    hole_block = pygame.image.load("images/hole_block.png")
    hole_block_edge = pygame.image.load("images/hole_block_edge.png")
    bill_spawn = pygame.image.load("images/bill_spawn.png")
    bull_spawn = pygame.image.load("images/bull_spawn.png")

    MAP = {'level' : 0, 'solids' : [], 'holes' : [], 'point' : 0, 'spawn' : []}
    loading_level = False
    moves = 0


    @staticmethod
    def create_tiles():

        for y in range(0, Tile.screen_size[1], Tile.height):
            for x in range(0, Tile.screen_size[0], Tile.width):
                if Tile.total_tiles in Tile.MAP['solids']:
                    Tile(x, y, 'solid')
                elif Tile.total_tiles == Tile.MAP ['point']:
                    Tile(x, y, 'point')
                elif Tile.total_tiles in Tile.MAP['holes']:
                    Tile(x, y, 'hole')
                elif Tile.total_tiles in Tile.MAP['spawn']:
                    if Tile.total_tiles == Tile.MAP['spawn'][0]:
                        Tile(x, y, 'spawnbill')
                    else:
                        Tile(x, y, 'spawnbull')
                else:
                    Tile(x, y, 'empty')

        for tile in Tile.List:
            if tile.type == 'empty':
                tile.walkable = False
            else:
                tile.walkable = True


    def __init__(self, x, y, Type):

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

        Tile.List.append(self)


    @staticmethod
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    def __str__(self):
        return str(self.number)
