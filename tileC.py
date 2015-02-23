import pygame, Funk

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

    #LEVEL 0 MAP PROPERTIES

    level = 0
    spawning_points = []
    valids = []
    holes = []
    meeting_point = 0

    loading_level = False

    @staticmethod
    def load_level(level): #SETS ALL LEVEL VARIABLES AND TILE TYPES ACCORDING TO LEVEL

        print 'Loading level {}...'.format(level)
        Tile.loading_level = True

        if level == 1:
            Tile.level = 1
            Tile.valids = [74, 75, 97, 119, 141, 142, 165, 144, 145, 167, 189, 211, 212, 213, 214, 215, 193, 171, 149, 127, 105, 104, 73, 95]
            Tile.holes = [72, 140]
            Tile.spawning_points = [(Tile.width * 16, Tile.height * 4), (Tile.width * 8, Tile.height * 3)] # bill, bull
            Tile.meeting_point = 143

        elif level == 2:
            Tile.level = 2
            Tile.valids = [186, 187, 188, 163, 141, 119, 118, 118, 117, 116, 138, 160, 182, 183, 205, 189, 167, 145, 146, 147, 170, 148, 192, 214, 234, 235, 236, 256, 278, 208, 190]
            Tile.holes = [191]
            Tile.spawning_points = [(Tile.width * 13, Tile.height * 12), (Tile.width * 6, Tile.height * 9)]
            Tile.meeting_point = 185

        elif level == 3:
            Tile.level = 3
            Tile.valids = [183, 205, 206, 207, 208, 210, 209, 211, 212, 213, 191, 169, 147, 125, 103, 75, 97, 119, 141, 163, 165, 164, 166, 167, 145, 123, 122, 121, 74, 73, 95, 124]
            Tile.holes = []
            Tile.spawning_points = [(Tile.width * 6, Tile.height * 4), (Tile.width * 6, Tile.height * 9)]
            Tile.meeting_point = 1

        elif level == 4:
            Tile.level = 4
            Tile.valids = [53, 54, 55, 56, 57, 101, 162, 163, 165, 164, 166, 161, 160, 116, 168, 191, 213, 214, 215, 237, 212, 211, 210, 209, 208, 186, 100, 98, 97, 96, 95, 94, 99, 79,138]
            Tile.holes = [167]
            Tile.spawning_points = [(Tile.width * 8, Tile.height * 2), (Tile.width * 16, Tile.height * 10)]
            Tile.meeting_point = 169

        elif level == 100:
            Tile.level = 100
            Tile.valids = []
            Tile.holes = []
            Tile.spawning_points = [(Tile.width * 6, Tile.height * 4), (Tile.width * 6, Tile.height * 9)]
            Tile.meeting_point = 1

        for tile in Tile.List: #SETS NEW TILE TYPES. SAME AS IN create_tiles FUNCTION, JUST REFRESHING FOR NEW MAP

            if tile.number in Tile.valids:
                tile.type = 'solid'
            elif tile.number == Tile.meeting_point:
                tile.type = 'point'
            elif tile.number in Tile.holes:
                tile.type = 'hole'
            else:
                tile.type = 'empty'

            if tile.type == 'empty':
                tile.walkable = False
            else:
                tile.walkable = True


    @staticmethod
    def create_tiles(): #SPLITS THE SCREEN INTO TILES AND GIVES THEM TYPES. (ONE TIME RUN)

        for y in range(0, Tile.screen_size[1], Tile.height):
            for x in range(0, Tile.screen_size[0], Tile.width):
                if Tile.total_tiles in Tile.valids:
                    Tile(x, y, 'solid')
                elif Tile.total_tiles == Tile.meeting_point:
                    Tile(x, y, 'point')
                elif Tile.total_tiles in Tile.holes:
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

        Funk.text_to_screen(screen, 'Level: ' + str(Tile.level), 20, 20, color = (0,0,0))

        if Tile.loading_level:
            pygame.time.Clock().tick(1)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





    @staticmethod
    def show_info(screen, bill, bull):

        for tile in Tile.List:
            Funk.text_to_screen(screen, tile.number, tile.x, tile.y)
            #Funk.text_to_screen(screen, str(tile.walkable), tile.x, tile.y + 10)

        solid, empty, hole = 0, 0, 0

        for tile in Tile.List:
            if tile.type == 'solid':
                solid += 1
            elif tile.type == 'empty':
                empty += 1
            elif tile.type == 'hole':
                hole += 1

        Funk.text_to_screen(screen, 'Solid blocks: ' + str(solid), 20, 40, color = (0,0,0))
        Funk.text_to_screen(screen, 'Hole blocks: ' + str(hole), 20, 60, color = (0,0,0))
        Funk.text_to_screen(screen, 'Empty blocks: ' + str(empty), 20, 80, color = (0,0,0))

        Funk.text_to_screen(screen, 'Bill position: ' + str(bill.get_number()), 20, 120, color = (0,0,0))
        Funk.text_to_screen(screen, 'Bull position: ' + str(bull.get_number()), 20, 140, color = (0,0,0))

    def __str__(self):
        return str(self.number)