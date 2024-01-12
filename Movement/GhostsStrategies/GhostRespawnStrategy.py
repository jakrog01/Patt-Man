from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy
from Movement.GhostsStrategies.GhostLeaveHouseStrategy import GhostLeaveHouseStrategy

from Sprite.AbstractGhost import AbstractGhost
from Sprite.Player import Player

from Movement.GhostsStrategies.RespawnPathfinder import get_next_move

class GhostRespawnStrategy(AbstractGhostStrategy):
    def __init__(self):
        self.__visited = []

    def choose_direction(self, ghost: AbstractGhost, player: Player, tile_size: int, map: list, distx: int, disty: int):
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
        
        
            