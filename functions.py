import pygame
from tileC import Tile

def text_to_screen(screen, text, x, y, size = 15, color = (255, 255, 255), font_type = 'monospace'):

    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
        
    except Exception, e:
        print 'Font error, saw it comming'
        raise e


def load_level(level): #SETS ALL LEVEL VARIABLES AND TILE TYPES ACCORDING TO LEVEL

    print 'Loading level {}...'.format(level)
    Tile.loading_level = True
    Tile.moves = 0 

    if level == 1:
    	Tile.MAP = {'point': 143, 'spawn': [105, 75], 'solids': [74, 75, 97, 119, 141, 142, 165, 144, 145, 167, 189, 211, 212, 213, 214, 215, 193, 171, 149, 127, 105, 104, 73, 95], 'holes': [72, 140], 'level': 1}

    elif level == 2:
        Tile.MAP = {'point': 164, 'spawn': [257, 211], 'solids': [165, 166, 167, 168, 146, 124, 125, 126, 149, 127, 171, 193, 213, 214, 215, 235, 257, 170, 189, 211], 'holes': [169], 'level': 2}

    elif level == 3:
        Tile.MAP = {'point': 143, 'spawn': [96, 101], 'solids': [141, 142, 165, 144, 145, 167, 163, 121, 99, 100, 119, 97, 96, 101], 'holes': [140], 'level': 3}

    elif level == 100:
    	Tile.MAP = {'point': 0, 'spawn': [0, 0], 'solids': [28, 50, 72, 94, 116, 29, 74, 52, 96, 117, 32, 54, 76, 98, 120, 121, 77, 33, 270, 226, 182, 274, 278, 190, 194, 238, 180, 202, 224, 246, 268, 181, 225, 269, 184, 206, 228, 250, 272, 273, 276, 254, 232, 210, 188, 277, 234, 212, 256, 189, 192, 214, 236, 258, 280, 237, 193, 216, 34, 78, 122, 36, 58, 80, 102, 125, 104, 82, 60, 38], 'holes': [], 'level': 100}

    for tile in Tile.List: #SETS NEW TILE TYPES. SAME AS IN Tile.create_tiles FUNCTION, JUST REFRESHING FOR NEW MAP

        if tile.number in Tile.MAP['solids']:
            tile.type = 'solid'
        elif tile.number == Tile.MAP['point']:
            tile.type = 'point'
        elif tile.number in Tile.MAP['holes']:
            tile.type = 'hole'
        else:
            tile.type = 'empty'

        if tile.type == 'empty':
            tile.walkable = False
        else:
            tile.walkable = True

    print 'Done!'