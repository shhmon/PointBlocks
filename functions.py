import pygame, csv, sys
from tileC import Tile
from characterC import Character

global state
state = 1

def text_to_screen(screen, text, x, y, size = 15, color = (255, 255, 255), font_type = 'monospace'):

    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
        
    except Exception, e:
        print 'Font error, saw it comming'
        raise e

def get_state():
    global state
    return state

def load_level(level = 1): #SETS ALL LEVEL VARIABLES AND TILE TYPES ACCORDING TO LEVEL

    try:

        List = []
        Tile.moves = 0

        print 'Loading level {}...'.format(level)
        filename = 'level/level{}.csv'.format(level)

        levelfile = open(filename)
        csv_levelfile = csv.reader(levelfile)

        i = 0

        Tile.clear_map_dict()

        for row in csv_levelfile:
            if i == 0:
                Tile.MAP['level'] = int(row[0])
            elif i == 1:
                for element in row:
                    Tile.MAP['spawn'].append(int(element))
            elif i == 2:
                Tile.MAP['point'] = int(row[0])
            elif i == 3:
                for element in row:
                    Tile.MAP['holes'].append(int(element))
            elif i == 4:
                for element in row:
                    Tile.MAP['solids'].append(int(element))
            elif i == 5:
                i = 0

            i += 1

        for character in Character.List:
            character.tx, character.ty = None, None
            character.unnatural = False

        levelfile.close()
        Tile.retype()
        Character.respawn()


    except Exception, e:
        print 'Could not load level {}'.format(level)
        pygame.quit()
        sys.exit()