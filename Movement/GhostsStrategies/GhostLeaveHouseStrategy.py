from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

from Sprite.AbstractGhost import AbstractGhost
from Sprite.Player import Player

class GhostLeaveHouseStrategy(AbstractGhostStrategy):
    def choose_direction(self, ghost: AbstractGhost, player: Player, tile_size: int, map: list, distx: int, disty: int):
        ghost_x = int(ghost.x // tile_size)
        ghost_y = int(ghost.y // tile_size)
        ghost.direction = "Up"
        
        if map[ghost_y-1][ghost_x] != 0 and map[ghost_y-1][ghost_x] != 9 and map[ghost_y-1][ghost_x] != 7 and map[ghost_y-1][ghost_x] != 8:
            if ghost.y % 11 == 10:
                ghost.enter_predator_mode()
        
            