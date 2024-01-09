from abc import ABC,abstractmethod
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter

class AbstractMovementVisitor(ABC):

    @abstractmethod
    def visitPacman(self, pacman: Pacman):
        raise NotImplemented