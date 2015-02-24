import pygame, functions

class Tile(pygame.Rect):

    #SCREEN & TILE SIZE PROPERTIES

    List = []
    freeze = False
    screen_size = (990, 675)
    width, height = 45, 45
    total_tiles = 1
    H, V = 1, 22

    # SPRITES

    solid_block = pygame.image.load("images/solid_block.png")
    solid_block_edge = pygame.image.load("images/solid_block_edge.png")
    point_block = pygame.image.load("images/point_block.png")
    point_block_edge = pygame.image.load("images/point_block_edge.png")
    hole_block = pygame.image.load("images/hole_block.png")
    hole_block_edge = pygame.image.load("images/hole_block_edge.png")

    #LEVEL PROPERTIES

    MAP = {'level' : 0, 'solids' : [], 'holes' : [], 'point' : 0, 'spawn' : []} #MAP: level, valdis, holes, point, spawn
    loading_level = False
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

        if Tile.loading_level:
            pygame.time.Clock().tick(1)

    def __str__(self):
        return str(self.number)
