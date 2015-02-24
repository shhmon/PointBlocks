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
    	Tile.MAP = {'point': 143, 'spawn': [(720, 180), (360, 135)], 'valids': [74, 75, 97, 119, 141, 142, 165, 144, 145, 167, 189, 211, 212, 213, 214, 215, 193, 171, 149, 127, 105, 104, 73, 95], 'holes': [72, 140], 'level': 1}

    elif level == 2:
        Tile.MAP = {'point': 164, 'spawn': [(630, 495), (315, 360)], 'valids': [165, 166, 167, 142, 120, 98, 97, 97, 96, 95, 117, 139, 161, 162, 184, 168, 146, 124, 125, 126, 149, 127, 171, 193, 213, 214, 215, 235, 257, 187, 170], 'holes': [169], 'level': 2}

    elif level == 3:
        Tile.MAP = {'point': 169, 'spawn': [(360, 90), (720, 450)], 'valids': [53, 54, 55, 56, 57, 101, 162, 163, 165, 164, 166, 161, 160, 116, 168, 191, 213, 214, 215, 237, 212, 211, 210, 209, 208, 186, 100, 98, 97, 96, 95, 94, 99, 79, 138], 'holes': [167], 'level': 3}

    elif level == 100:
    	Tile.MAP = {'point': 1, 'spawn': [(1, 1), (1, 1)], 'valids': [], 'holes': [], 'level': 100}

    for tile in Tile.List: #SETS NEW TILE TYPES. SAME AS IN Tile.create_tiles FUNCTION, JUST REFRESHING FOR NEW MAP

        if tile.number in Tile.MAP['valids']:
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