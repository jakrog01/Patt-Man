from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy
from Movement.GhostsStrategies.GhostLeaveHouseStrategy import GhostLeaveHouseStrategy
from Movement.GhostsStrategies.RespawnPathfinder import get_next_move

class GhostRespawnStrategy(AbstractGhostStrategy):
    def __init__(self):
        self.__visited = []

    def choose_direction(self, ghost, player, tile_size, map, distx, disty):
        ghost_x = int(ghost.x // tile_size)
        ghost_y = int(ghost.y // tile_size)
        next_move = get_next_move(map, ghost_x, ghost_y, ghost.respawn_x, ghost.respawn_y)
        if next_move != "None":
            ghost.direction = next_move
        elif next_move == "None":
            ghost.inverse_direction()
        
        if ghost_x == ghost.respawn_x and ghost_y == ghost.respawn_y:
            ghost.enter_predator_mode()
            ghost.strategy = GhostLeaveHouseStrategy()
            ghost.state = "Escape"
        
        
            