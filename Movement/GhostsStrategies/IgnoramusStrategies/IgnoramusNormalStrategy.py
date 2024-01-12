from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy
from math import sqrt

from Sprite.AbstractGhost import AbstractGhost
from Sprite.Player import Player

class IgnoramusNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, ignoramus: AbstractGhost, player: Player, tile_size: int, map: list, distx: int, disty: int):
        ignoramus_x = int(ignoramus.x // tile_size)
        ignoramus_y = int(ignoramus.y // tile_size)

        player_x = int(player.x // tile_size)
        player_y = int(player.y // tile_size)

        distance_to_player = (ignoramus_x - player_x) **2 + (ignoramus_y + player_y)**2

        if sqrt(distance_to_player) > 8:
            destination_x = int(player.x // tile_size)
            destination_y = int(player.y // tile_size)
        else:
            destination_x = distx
            destination_y = disty

        distance = 1000000
        new_direction = "None"

        if ignoramus.direction != "Left":
            if map[ignoramus_y][ignoramus_x+1] == 9 or map[ignoramus_y][ignoramus_x+1] == 0 or map[ignoramus_y][ignoramus_x+1] == 8 or map[ignoramus_y][ignoramus_x+1] == 10:
                new_distance = ((ignoramus_x+1) - destination_x)**2 + (ignoramus_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if ignoramus.direction != "Right":
            if map[ignoramus_y][ignoramus_x-1] == 9 or map[ignoramus_y][ignoramus_x-1] == 0  or map[ignoramus_y][ignoramus_x-1] == 8 or map[ignoramus_y][ignoramus_x-1] == 10:
                new_distance = ((ignoramus_x-1) - destination_x)**2 + (ignoramus_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if ignoramus.direction != "Up":
            if map[ignoramus_y+1][ignoramus_x] == 9 or map[ignoramus_y+1][ignoramus_x] == 0 or map[ignoramus_y+1][ignoramus_x] == 8 or map[ignoramus_y+1][ignoramus_x] == 10:
                new_distance = (ignoramus_x - destination_x)**2 + ((ignoramus_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if ignoramus.direction != "Down":
            if map[ignoramus_y-1][ignoramus_x] == 9 or map[ignoramus_y-1][ignoramus_x] == 0 or map[ignoramus_y-1][ignoramus_x] == 7 or map[ignoramus_y-1][ignoramus_x] == 8 or map[ignoramus_y-1][ignoramus_x] == 10:
                new_distance = (ignoramus_x - destination_x)**2 + ((ignoramus_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
           ignoramus.inverse_direction()
        else:
            ignoramus.direction = new_direction
        
            