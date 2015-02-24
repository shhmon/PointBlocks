import pygame, sys
from tileC import Tile
from object_classes import *

def build_controls(screen):

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    block_type = 'hole'

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print Tile.MAP
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):

                        if block_type == 'solid':
                            if tile.type == 'empty':
                                Tile.MAP['solids'].append(tile.number)
                            elif tile.number == Tile.MAP['point']:
                                tile.MAP['point'] = 0
                            elif tile.number in Tile.MAP['holes']:
                                Tile.MAP['holes'].remove(tile.number)

                        if block_type == 'point':
                            if tile.type == 'empty':
                                if Tile.get_tile(Tile.MAP['point']) in Tile.List:
                                    Tile.get_tile(Tile.MAP['point']).type = 'empty'
                                Tile.MAP['point'] = tile.number
                            if tile.number in Tile.MAP['solids']:
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number in Tile.MAP['holes']:
                                Tile.MAP['holes'].remove(tile.number)

                        if block_type == 'hole':
                            if tile.type == 'empty':
                                Tile.MAP['holes'].append(tile.number)
                            if tile.number in Tile.MAP['solids']:
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number == Tile.MAP['point']:
                                Tile.MAP['point'] = 0

                        tile.type = block_type
                        print 'Trying to create: ', tile.type, ' on tile: ', tile.number
                        tile.walkable = True

            elif event.button == RIGHT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):

                        if tile.type == 'point':
                            Tile.MAP['point'] = 0
                        else:
                            if tile.number in Tile.MAP['solids']:
                                Tile.MAP['solids'].remove(tile.number)
                            elif tile.number in Tile.MAP['holes']:
                                Tile.MAP['holes'].remove(tile.number)

                        print 'Trying to remove: ', tile.type, ' on tile: ', tile.number
                        tile.type = 'empty'
                        tile.walkable = False

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