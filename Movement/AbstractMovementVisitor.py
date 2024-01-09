from abc import ABC,abstractmethod
from Sprite.Player import Player
from Sprite.Hunter import Hunter

class AbstractMovementVisitor(ABC):

    @abstractmethod
    def visit_player(self, pacman: Player):
        raise NotImplemented