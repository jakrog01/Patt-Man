from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class GhostDispersionStrategy(AbstractGhostStrategy):
    def choose_direction(self, ghost, pacman, tile_size, map, distx, disty):

        ghost_x = int(ghost.x // tile_size)
        ghost_y = int(ghost.y // tile_size)

        destination_x = distx
        destination_y = disty

        distance = 1000000
        new_direction = "None"

        if ghost.direction != "Left":
            if map[ghost_y][ghost_x+1] == 9 or map[ghost_y][ghost_x+1] == 0 or map[ghost_y][ghost_x+1] == 8:
                new_distance = ((ghost_x+1) - destination_x)**2 + (ghost_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if ghost.direction != "Right":
            if map[ghost_y][ghost_x-1] == 9 or map[ghost_y][ghost_x-1] == 0 or map[ghost_y][ghost_x-1] == 8:
                new_distance = ((ghost_x-1) - destination_x)**2 + (ghost_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if ghost.direction != "Up":
            if map[ghost_y+1][ghost_x] == 9 or map[ghost_y+1][ghost_x] == 0 or  map[ghost_y+1][ghost_x] == 8: 
                new_distance = (ghost_x - destination_x)**2 + ((ghost_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if ghost.direction != "Down":
            if map[ghost_y-1][ghost_x] == 9 or map[ghost_y-1][ghost_x] == 0 or map[ghost_y-1][ghost_x] == 7 or map[ghost_y-1][ghost_x] == 8:
                new_distance = (ghost_x - destination_x)**2 + ((ghost_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
            ghost.inverse_direction()
        else:
            ghost.direction = new_direction
        
            