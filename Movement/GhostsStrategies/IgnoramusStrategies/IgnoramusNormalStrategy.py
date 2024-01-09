from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy
from math import sqrt

class IgnoramusNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, ignoramus, pacman, tile_size, map, distx, disty):
        ignoramus_x = int(ignoramus.x // tile_size)
        ignoramus_y = int(ignoramus.y // tile_size)

        pacman_x = int(pacman.x // tile_size)
        pacman_y = int(pacman.y // tile_size)

        distance_to_pacman = (ignoramus_x - pacman_x) **2 + (ignoramus_y + pacman_y)**2

        if sqrt(distance_to_pacman) > 8:
            destination_x = int(pacman.x // tile_size)
            destination_y = int(pacman.y // tile_size)
        else:
            destination_x = distx
            destination_y = disty

        distance = 1000000
        new_direction = "None"

        if ignoramus.direction != "Left":
            if map[ignoramus_y][ignoramus_x+1] == 9 or map[ignoramus_y][ignoramus_x+1] == 0 or map[ignoramus_y][ignoramus_x+1] == 8:
                new_distance = ((ignoramus_x+1) - destination_x)**2 + (ignoramus_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if ignoramus.direction != "Right":
            if map[ignoramus_y][ignoramus_x-1] == 9 or map[ignoramus_y][ignoramus_x-1] == 0  or map[ignoramus_y][ignoramus_x-1] == 8:
                new_distance = ((ignoramus_x-1) - destination_x)**2 + (ignoramus_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if ignoramus.direction != "Up":
            if map[ignoramus_y+1][ignoramus_x] == 9 or map[ignoramus_y+1][ignoramus_x] == 0 or map[ignoramus_y+1][ignoramus_x] == 8:
                new_distance = (ignoramus_x - destination_x)**2 + ((ignoramus_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if ignoramus.direction != "Down":
            if map[ignoramus_y-1][ignoramus_x] == 9 or map[ignoramus_y-1][ignoramus_x] == 0 or map[ignoramus_y-1][ignoramus_x] == 7 or map[ignoramus_y-1][ignoramus_x] == 8:
                new_distance = (ignoramus_x - destination_x)**2 + ((ignoramus_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
           ignoramus.inverse_direction()
        else:
            ignoramus.direction = new_direction
        
            