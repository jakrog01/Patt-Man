from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class GhostLeaveHouseStrategy(AbstractGhostStrategy):
    def choose_direction(self, ghost, pacman, tile_size, map, distx, disty):
        ghost_x = int(ghost.x // tile_size)
        ghost_y = int(ghost.y // tile_size)
        ghost.direction = "Up"
        
        if map[ghost_y-1][ghost_x] == 1:
            if ghost.y % 11 == 10:
                ghost.enter_predator_mode()
        
            