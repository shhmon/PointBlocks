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
    point_block = pygame.image.load("images/point_block.gif")
    point_block_edge = pygame.image.load("images/point_block_edge.gif")
    hole_block = pygame.image.load("images/hole_block.png")
    hole_block_edge = pygame.image.load("images/hole_block_edge.png")

    level = 0
    spawning_points = []
    valids = []
    holes = []
    meeting_point = 0

    @staticmethod
    def load_level(level): #sets all level variables and gives new types to tiles accordingly

        # MAP PROPERTIES
        if level == 1:
            Tile.level = 1
            Tile.valids = [74, 75, 97, 119, 141, 140, 139, 142, 165, 144, 145, 167, 189, 211, 212, 213, 214, 215, 193, 171, 149, 127, 105, 104, 73, 95]
            Tile.holes = [72, 138]
            Tile.spawning_points = [(720, 180), (360, 135)] # bill, bull
            Tile.meeting_point = 143

        elif level == 2:
            print "loading level 2"
            Tile.level = 2
            Tile.valids = [74, 75, 97, 119, 141, 140, 139, 142, 165, 144, 145, 167, 189, 211, 212, 213, 214, 215, 193, 171, 149, 127, 105, 104, 73, 95, 244, 266, 288, 289, 247, 269, 291, 292, 293, 271, 249, 248, 251, 273, 295, 296, 255, 256, 257, 279, 300, 301, 302, 303, 281]
            Tile.holes = [2, 3, 4, 5]
            Tile.spawning_points = [(720, 180), (360, 135)]
            Tile.meeting_point = 143

        for tile in Tile.List:
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
    def create_tiles(): #splits the playscreen into tiles with tiles

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


    def __init__(self, x, y, Type):

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = False
        else:
            self.walkable = True

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

        Tile.List.append(self)


    @staticmethod
    def get_tile(number): #returns a tile object if passed the objects number
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tiles(screen):
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

    @staticmethod
    def show_info(screen, bill, bull):

        #for tile in Tile.List:
            #Funk.text_to_screen(screen, tile.number, tile.x, tile.y)
        #Funk.text_to_screen(screen, str(tile.walkable), tile.x, tile.y + 10)

        solid, empty, hole = 0, 0, 0

        for tile in Tile.List:
            if tile.type == 'solid':
                solid += 1
            elif tile.type == 'empty':
                empty += 1
            elif tile.type == 'hole':
                hole += 1

        Funk.text_to_screen(screen, 'Level: ' + str(Tile.level), 20, 20, color = (0,0,0))
        Funk.text_to_screen(screen, 'Solid blocks: ' + str(solid), 20, 40, color = (0,0,0))
        Funk.text_to_screen(screen, 'Hole blocks: ' + str(hole), 20, 60, color = (0,0,0))
        Funk.text_to_screen(screen, 'Empty blocks: ' + str(empty), 20, 80, color = (0,0,0))

        Funk.text_to_screen(screen, 'Bill position: ' + str(bill.get_number()), 20, 120, color = (0,0,0))
        Funk.text_to_screen(screen, 'Bull position: ' + str(bull.get_number()), 20, 140, color = (0,0,0))
        Funk.text_to_screen(screen, 'Valids: ' + str(Tile.valids), 20, 600, size = 8, color = (0,0,0))

    def __str__(self):
        return str(self.number)