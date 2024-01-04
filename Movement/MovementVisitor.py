from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Movement.PacmanMovementCommands.MovementManager import MovementManager
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter

class MovementVisitor(AbstractMovementVisitor):
    def __init__(self, map, title_size):
        self.__map = map
        self.__title_size = title_size

        self.__pacman_manager = MovementManager(self.__map, self.__title_size)

    
    def visitPacman(self, pacman: Pacman):
        self.__pacman_manager.move(pacman)

    def visitHunter(self, hunter: Hunter):
        pass