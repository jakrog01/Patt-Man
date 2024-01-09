from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Movement.PlayerMovementCommands.PlayerMovementManager import PlayerMovementManager
from Movement.GhostsMovementCommands.GhostMovementManager import GhostsMovementManager
from Sprite.Player import Player
from Sprite.AbstractGhost import AbstractGhost

class MovementVisitor(AbstractMovementVisitor):
    def __init__(self, map, title_size, ghosts):
        self.__map = map
        self.__title_size = title_size

        self.__player_manager = PlayerMovementManager(self.__map, self.__title_size, ghosts)
        self.__ghost_manager = GhostsMovementManager(self.__map, self.__title_size)

    def visit_player(self, player: Player):
        self.__player_manager.move(player)

    def visit_ghost(self, ghost: AbstractGhost):
        self.__ghost_manager.move(ghost)