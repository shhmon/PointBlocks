import pygame, sys, csv
from tileC import Tile
from Tkinter import *
from object_classes import Character

root = Tk()
global testing
testing = False

def clearmap():
    global testing
    testing = False
    print 'Clearing map...'

    for tile in Tile.List:
        tile.type = 'empty'
        tile.walkable = False

    Tile.MAP['solids'] = []
    Tile.MAP['point'] = 0
    Tile.MAP['holes'] = []
    Tile.MAP['spawn'] = []

    print 'Sucess!'

def openfile():

    try:
        filename = 'level/{}.csv'.format(name_entry.get())
        levelfile = open(filename)

        csv_levelfile = csv.reader(levelfile)

        i = 0
        for row in csv_levelfile:
            if i == 0:
                Tile.MAP['level'] = int(row[0])
                print 'Level set to: {}'.format(Tile.MAP['level'])
            elif i == 1:
                if Tile.MAP['spawn'] != []:
                    Tile.MAP['spawn'] = []
                for element in row:
                    Tile.MAP['spawn'].append(int(element))
                print 'Spawn set to: {}'.format(Tile.MAP['spawn'])
            elif i == 2:
                Tile.MAP['point'] = int(row[0])
                print 'Point set to: {}'.format(Tile.MAP['point'])
            elif i == 3:
                if Tile.MAP['holes'] != []:
                    Tile.MAP['holes'] = []
                for element in row:
                    Tile.MAP['holes'].append(int(element))
                print 'Holes set to: {}'.format(Tile.MAP['holes'])
            elif i == 4:
                if Tile.MAP['solids'] != []:
                    Tile.MAP['solids'] = []
                for element in row:
                    Tile.MAP['solids'].append(int(element))
                print 'Holids set to: {}'.format(Tile.MAP['solids'])
            elif i == 5:
                i = 0

            i += 1

        levelfile.close()

    except Exception, e:
        print "Hmm... Doesn't look like the file '{}' exists.".format(name_entry.get())



def savemap():

    try:

        levelfile = 'level/{}.csv'.format(name_entry.get())

        row0 = []
        row0.append(str(Tile.MAP['level']))
        row1 = []
        row2 = Tile.MAP['point']
        row3 = []
        row4 = []

        for value in Tile.MAP['spawn']:
            row1.append(str(value))
        for value in Tile.MAP['holes']:
            row3.append(str(value))
        for value in Tile.MAP['solids']:
            row4.append(str(value))

        print row0, row1, row2, row3, row4

        with open(levelfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(row0)
            writer.writerow(row1)
            writer.writerow([row2])
            writer.writerow(row3)
            writer.writerow(row4)

    except Exception, e:
        print 'Error saving map.'

def testplay():
    global testing

    if testing == False:
        testing = True
        Tile.loading_level = True
    else:
        testing = False


types = ['solid', 'point', 'hole', 'spawnbill', 'spawnbull']
block_default = StringVar(root)
block_default.set(types[0])

name = StringVar(root)

empty_label = Label(root)
block_menu = apply(OptionMenu, (root, block_default) + tuple(types))
blocktype_label = Label(root, text="Block type: ")
name_label = Label(root, text="File name: .csv")
clear_button = Button(root, text="Clear map", command=clearmap)
name_entry = Entry(root, textvariable=name)
save_button = Button(root, text="Save file", command=savemap)
open_button = Button(root, text="Open file", command=openfile)
play_button = Button(root, text="Start/Stop Test", command=testplay)


block_menu.configure(width=20)
clear_button.configure(width=20)
save_button.configure(width=20)
open_button.configure(width=20)
empty_label.configure(height=12)
play_button.configure(width=20)

blocktype_label.pack()
block_menu.pack()
clear_button.pack()
play_button.pack()
empty_label.pack()
name_label.pack()
name_entry.pack()
open_button.pack()
save_button.pack()

root.geometry("10x400")

def show_inter_window():
    root.update()

def build_controls(screen):

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    block_type = block_default.get()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print Tile.MAP
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):

                        print 'Trying to create {} block on tile: {}'.format(block_type, tile.number)

                        if block_type == 'solid':
                            if tile.type == 'empty':
                                Tile.MAP['solids'].append(tile.number)
                            elif tile.number == Tile.MAP['point']:
                                tile.MAP['point'] = 0
                            elif tile.number in Tile.MAP['holes']:
                                Tile.MAP['holes'].remove(tile.number)

                        elif block_type == 'point':
                            if tile.type == 'empty':
                                if Tile.get_tile(Tile.MAP['point']) in Tile.List:
                                    Tile.get_tile(Tile.MAP['point']).type = 'empty'
                                    Tile.get_tile(Tile.MAP['point']).walkable = False
                                Tile.MAP['point'] = tile.number
                            if tile.number in Tile.MAP['solids']:
                                if Tile.get_tile(Tile.MAP['point']) in Tile.List:
                                    Tile.get_tile(Tile.MAP['point']).type = 'empty'
                                    Tile.get_tile(Tile.MAP['point']).walkable = False
                                Tile.MAP['point'] = tile.number
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number in Tile.MAP['holes']:
                                if Tile.get_tile(Tile.MAP['point']) in Tile.List:
                                    Tile.get_tile(Tile.MAP['point']).type = 'empty'
                                    Tile.get_tile(Tile.MAP['point']).walkable = False
                                Tile.MAP['point'] = tile.number
                                Tile.MAP['holes'].remove(tile.number)

                        elif block_type == 'hole':
                            if tile.type == 'empty':
                                Tile.MAP['holes'].append(tile.number)
                            if tile.number in Tile.MAP['solids']:
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number == Tile.MAP['point']:
                                Tile.MAP['point'] = 0

                        elif block_type == 'spawnbill':
                            elements = 0
                            for i in range(0, Tile.total_tiles + 1):
                                if i in Tile.MAP['spawn']:
                                    elements +=1

                            if elements == 1:
                                Tile.MAP['spawn'].append(1)
                            elif elements > 2 or elements == 0:
                                Tile.MAP['spawn'] = [1,1]

                            if tile.type == 'empty':
                                if Tile.get_tile(Tile.MAP['spawn'][0]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][0]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][0]).walkable = False
                                Tile.MAP['spawn'][0] = tile.number

                            if tile.number in Tile.MAP['solids']:
                                if Tile.get_tile(Tile.MAP['spawn'][0]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][0]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][0]).walkable = False
                                Tile.MAP['spawn'][0] = tile.number

                            elif tile.number in Tile.MAP['holes']:
                                if Tile.get_tile(Tile.MAP['spawn'][0]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][0]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][0]).walkable = False
                                Tile.MAP['spawn'][0] = tile.number
                                Tile.MAP['holes'].remove(tile.number)

                        elif block_type == 'spawnbull':
                            elements = 0
                            for i in range(0, Tile.total_tiles + 1):
                                if i in Tile.MAP['spawn']:
                                    elements +=1
                            if elements == 1:
                                Tile.MAP['spawn'].append(1)
                            elif elements > 2 or elements == 0:
                                Tile.MAP['spawn'] = [1,1]

                            if tile.type == 'empty':
                                if Tile.get_tile(Tile.MAP['spawn'][1]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][1]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][1]).walkable = False
                                Tile.MAP['spawn'][1] = tile.number

                            if tile.number in Tile.MAP['solids']:
                                if Tile.get_tile(Tile.MAP['spawn'][1]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][1]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][1]).walkable = False
                                Tile.MAP['spawn'][1] = tile.number

                            elif tile.number in Tile.MAP['holes']:
                                if Tile.get_tile(Tile.MAP['spawn'][1]) in Tile.List:
                                    Tile.get_tile(Tile.MAP['spawn'][1]).type = 'empty'
                                    Tile.get_tile(Tile.MAP['spawn'][1]).walkable = False
                                Tile.MAP['spawn'][1] = tile.number
                                Tile.MAP['holes'].remove(tile.number)

                        tile.type = block_type
                        tile.walkable = True

                        if Tile.get_tile(tile.number).type == block_type:
                            print 'Success!'
                        else:
                            print 'Failed.'

            elif event.button == RIGHT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):

                        i = 0

                        if tile.type == 'empty':
                            print 'Tile is already empty.'
                        else:
                            print 'Trying to remove {} block from tile: {}'.format(tile.type, tile.number)
                            i = 1

                        if tile.type == 'point':
                            Tile.MAP['point'] = 0
                        else:
                            if tile.number in Tile.MAP['solids']:
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number in Tile.MAP['holes']:
                                Tile.MAP['holes'].remove(tile.number)
                            elif tile.number in Tile.MAP['spawn']:
                                Tile.MAP['spawn'].remove(tile.number)

                        tile.type = 'empty'
                        tile.walkable = False

                        if tile.type == 'empty' and i == 1:
                            print 'Sucess!'
                        else:
                            print 'Failed.'



def draw_tiles(screen):
    for tile in Tile.List:
        pygame.draw.aaline(screen, (100,100,100), (tile.x, tile.y), (tile.x, tile.y + Tile.height))
        pygame.draw.aaline(screen, (100,100,100), (tile.x, tile.y + Tile.height), (tile.x + Tile.width, tile.y + Tile.height))
        if (tile.walkable):
            if tile.number < Tile.total_tiles - Tile.V:
                tile_below = Tile.get_tile(tile.number + Tile.V)
                if (tile_below.walkable):
                    if tile.type == 'point':
                        screen.blit(Tile.point_block, (tile))
                    elif tile.type == 'hole':
                        screen.blit(Tile.hole_block, (tile))
                    elif tile.type == 'spawnbill':
                        screen.blit(Tile.bill_spawn, (tile))
                    elif tile.type == 'spawnbull':
                        screen.blit(Tile.bull_spawn, (tile))
                    else:
                        screen.blit(Tile.solid_block, (tile))
                else:
                    if tile.type == 'point':
                        screen.blit(Tile.point_block_edge, (tile))
                    elif tile.type == 'hole':
                        screen.blit(Tile.hole_block_edge, (tile))
                    elif tile.type == 'spawnbill':
                        screen.blit(Tile.bill_spawn, (tile))
                    elif tile.type == 'spawnbull':
                        screen.blit(Tile.bull_spawn, (tile))
                    else:
                        screen.blit(Tile.solid_block_edge, (tile))



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


def show_info(screen):

    for tile in Tile.List:
        functions.text_to_screen(screen, tile.number, tile.x, tile.y)
        #functions.text_to_screen(screen, str(tile.walkable), tile.x, tile.y + 10)

    solid, empty, hole = 0, 0, 0

    for tile in Tile.List:
        if tile.type == 'solid':
            solid += 1
        elif tile.type == 'empty':
            empty += 1
        elif tile.type == 'hole':
            hole += 1

    functions.text_to_screen(screen, 'Solid blocks: ' + str(solid), 20, 140, color = (0,0,0))
    functions.text_to_screen(screen, 'Hole blocks: ' + str(hole), 20, 160, color = (0,0,0))
    functions.text_to_screen(screen, 'Empty blocks: ' + str(empty), 20, 180, color = (0,0,0))