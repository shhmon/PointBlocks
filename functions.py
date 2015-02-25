import pygame, csv
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


def load_level(level = 1): #SETS ALL LEVEL VARIABLES AND TILE TYPES ACCORDING TO LEVEL

    print 'Loading level {}...'.format(level)
    Tile.loading_level = True
    Tile.moves = 0
    filename = 'level/level{}.csv'.format(level)

    levelfile = open(filename)

    csv_levelfile = csv.reader(levelfile)

    i = 0

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

    levelfile.close()

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