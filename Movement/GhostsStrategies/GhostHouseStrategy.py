from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class GhostHouseStrategy(AbstractGhostStrategy):
    def choose_direction(self, ghost, pacman, tile_size, map, distx, disty):
        ghost_x = int(ghost.x // tile_size)
        ghost_y = int(ghost.y // tile_size)

        new_direction = "None"

        if ghost.direction == "Left":
            if map[ghost_y][ghost_x-1] != 9 and map[ghost_y][ghost_x-1] != 0:
                new_direction = "Right"
        else:
            if map[ghost_y][ghost_x+1] != 9 and map[ghost_y][ghost_x+1] != 0:
                new_direction = "Left"

        if new_direction == "None":
            ghost.inverse_direction()
        else:
            ghost.direction = new_direction
        
            