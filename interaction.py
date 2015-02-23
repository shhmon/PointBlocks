import pygame, sys
from tileC import Tile
from object_classes import Character

def interaction(screen, bill):

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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



    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: # North
        future_tile_number = player.get_number() - Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            for character in Character.List:
                if future_tile.walkable:
                    player.set_target(future_tile)

    if keys[pygame.K_s]: # South
        future_tile_number = player.get_number() + Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)

    if keys[pygame.K_a]: # West
        future_tile_number = player.get_number() - Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)

    if keys[pygame.K_d]: # East
        future_tile_number = player.get_number() + Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)



        """if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w: # North
                future_tile_number = player.get_number() - Tile.V

                if Tile.get_tile(future_tile_number).walkable:
                    player.y -= player.height                   

            if event.key == pygame.K_s: # South
                future_tile_number = player.get_number() + Tile.V

                if Tile.get_tile(future_tile_number).walkable:
                    player.y += player.height 

            if event.key == pygame.K_a: # West
                future_tile_number = player.get_number() - Tile.H

                if Tile.get_tile(future_tile_number).walkable:
                    player.x -= player.width 

            if event.key == pygame.K_d: # East
                future_tile_number = player.get_number() + Tile.H

                if Tile.get_tile(future_tile_number).walkable:
                    player.x += player.width """