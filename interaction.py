import pygame, sys
from tileC import Tile
from object_classes import Character

def interaction(screen, bill, bull):

#///////////////////////////////////////////////////////////////////////DEVELOP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == RIGHT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):
                        tile.type = 'point'
                        tile.walkable = True
                        if tile.number in Tile.valids:
                            Tile.valids.remove(tile.number)
                        Tile.meeting_point = tile.number
                        Tile.load_level(0)
                        print 'MP: ' + str(Tile.meeting_point)
                        break
            elif event.button == LEFT:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width) and tile.number not in Tile.valids:
                        tile.type = 'solid'
                        tile.walkable = True
                        Tile.valids.append(tile.number)
                        print 'Valids: ' + str(Tile.valids)
                        break

            elif event.button == MIDDLE:
                for tile in Tile.List:
                    if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):
                        tile.type = 'hole'
                        tile.walkable = True
                        if tile.number in Tile.valids:
                            Tile.valids.remove(tile.number)
                        Tile.holes.append(tile.number)
                        Tile.load_level(0)
                        print 'Holes: ' + str(Tile.holes)
                        break

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

    if keys[pygame.K_w] and not bill.has_target() and not bull.has_target(): # North

        future_tile_number_bill = bill.get_number() - Tile.V
        future_tile_number_bull = bull.get_number() - Tile.V

        if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

            if future_tile_number_bull == Tile.meeting_point and not Tile.get_tile(future_tile_number_bill).walkable:
                bull.set_target(Tile.get_tile(future_tile_number_bull))

            if future_tile_number_bill != bull.get_number():
                if Tile.get_tile(future_tile_number_bill).walkable:
                    bill.set_target(Tile.get_tile(future_tile_number_bill))

            if future_tile_number_bull != bill.get_number():
                if Tile.get_tile(future_tile_number_bull).walkable:
                    bull.set_target(Tile.get_tile(future_tile_number_bull))

#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

    if keys[pygame.K_s] and not bill.has_target() and not bull.has_target(): # South

        future_tile_number_bill = bill.get_number() + Tile.V
        future_tile_number_bull = bull.get_number() + Tile.V

        if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

            if future_tile_number_bull == Tile.meeting_point and not Tile.get_tile(future_tile_number_bill).walkable:
                bull.set_target(Tile.get_tile(future_tile_number_bull))

            if future_tile_number_bill != bull.get_number():
                if Tile.get_tile(future_tile_number_bill).walkable:
                    bill.set_target(Tile.get_tile(future_tile_number_bill))

            if future_tile_number_bull != bill.get_number():
                if Tile.get_tile(future_tile_number_bull).walkable:
                    bull.set_target(Tile.get_tile(future_tile_number_bull))

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    if keys[pygame.K_a] and not bill.has_target() and not bull.has_target(): # West

        future_tile_number_bill = bill.get_number() - Tile.H
        future_tile_number_bull = bull.get_number() - Tile.H

        if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

            if future_tile_number_bull == Tile.meeting_point and not Tile.get_tile(future_tile_number_bill).walkable:
                bull.set_target(Tile.get_tile(future_tile_number_bull))

            if future_tile_number_bill != bull.get_number():
                if Tile.get_tile(future_tile_number_bill).walkable:
                    bill.set_target(Tile.get_tile(future_tile_number_bill))

            if future_tile_number_bull != bill.get_number():
                if Tile.get_tile(future_tile_number_bull).walkable:
                    bull.set_target(Tile.get_tile(future_tile_number_bull))

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

    if keys[pygame.K_d] and not bill.has_target() and not bull.has_target(): # East

        future_tile_number_bill = bill.get_number() + Tile.H
        future_tile_number_bull = bull.get_number() + Tile.H

        if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

            if future_tile_number_bull == Tile.meeting_point and not Tile.get_tile(future_tile_number_bill).walkable:
                bull.set_target(Tile.get_tile(future_tile_number_bull))

            if future_tile_number_bill != bull.get_number():
                if Tile.get_tile(future_tile_number_bill).walkable:
                    bill.set_target(Tile.get_tile(future_tile_number_bill))

            if future_tile_number_bull != bill.get_number():
                if Tile.get_tile(future_tile_number_bull).walkable:
                    bull.set_target(Tile.get_tile(future_tile_number_bull))



    """if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w: # North
                future_tile_number_bill = bill.get_number() - Tile.V
                future_tile_number_bull = bull.get_number() - Tile.V

                if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

                    future_tile_bill = Tile.get_tile(future_tile_number_bill)
                    future_tile_bull = Tile.get_tile(future_tile_number_bull)

                    if future_tile_number_bill != bull.get_number():

                        print 'NORTH: bill future target is not bulls tile'

                        if future_tile_bill.walkable:
                            bill.set_target(future_tile_bill)

                    if future_tile_number_bull != bill.get_number():

                        print 'NORTH: bull future target is not bills tile'

                        if future_tile_bull.walkable:
                            bull.set_target(future_tile_bull)"""