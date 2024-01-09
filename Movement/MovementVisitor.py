from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Movement.PacmanMovementCommands.PacmanMovementManager import PacmanMovementManager
from Movement.GhostsMovementCommands.GhostMovementManager import GhostsMovementManager
from Sprite.Pacman import Pacman
from Sprite.AbstractGhost import AbstractGhost

class MovementVisitor(AbstractMovementVisitor):
    def __init__(self, map, title_size, ghosts):
        self.__map = map
        self.__title_size = title_size

        self.__pacman_manager = PacmanMovementManager(self.__map, self.__title_size, ghosts)
        self.__ghost_manager = GhostsMovementManager(self.__map, self.__title_size)

    
    def visitPacman(self, pacman: Pacman):
        self.__pacman_manager.move(pacman)

    def visit_ghost(self, ghost: AbstractGhost):
        self.__ghost_manager.move(ghost)