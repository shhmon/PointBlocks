import pygame, sys, functions
from tileC import Tile
from characterC import Character
from menuC import *

def menu_interaction(screen):

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0]
    My = Mpos[1]

    for button in Button.List:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if Mx >= button.x and Mx <= button.x + button.width and My > button.y and My <= button.y + button.height:

                button.color = (0,124,107)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.action == 'PLAY':
                        functions.state = 2
                    if button.action == 'DEVELOP':
                        print 'bajs'
            else:
                button.color = (255,255,255)

def interaction(screen, bill, bull):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

    if keys[pygame.K_w] and not bill.has_target() and not bull.has_target(): # North

        future_tile_number_bill = bill.get_number() - Tile.V
        future_tile_number_bull = bull.get_number() - Tile.V

        if future_tile_number_bill and future_tile_number_bull in range(1, Tile.total_tiles + 1):

                if future_tile_number_bull == Tile.MAP['point'] and not Tile.get_tile(future_tile_number_bill).walkable:
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

            if future_tile_number_bull == Tile.MAP['point'] and not Tile.get_tile(future_tile_number_bill).walkable:
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

            if future_tile_number_bull == Tile.MAP['point'] and not Tile.get_tile(future_tile_number_bill).walkable:
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

            if future_tile_number_bull == Tile.MAP['point'] and not Tile.get_tile(future_tile_number_bill).walkable:
                bull.set_target(Tile.get_tile(future_tile_number_bull))

            if future_tile_number_bill != bull.get_number():
                if Tile.get_tile(future_tile_number_bill).walkable:
                    bill.set_target(Tile.get_tile(future_tile_number_bill))

            if future_tile_number_bull != bill.get_number():
                if Tile.get_tile(future_tile_number_bull).walkable:
                    bull.set_target(Tile.get_tile(future_tile_number_bull))

    if keys[pygame.K_u] and not bill.has_target() and not bull.has_target(): # North
        bill.unnatural = True
        bill.set_target(Tile.get_tile(Tile.MAP['spawn'][1]))

    if keys[pygame.K_ESCAPE]:
        functions.state = 3