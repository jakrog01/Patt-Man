from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter

class MovementVisitor(AbstractMovementVisitor):
    def __init__(self, map, title_size):
        self.__map = map
        self.__title_size = title_size

    
    def visitPacman(self, pacman: Pacman):
        pass

    def visitHunter(self, hunter: Hunter):
        pass