from abc import ABC,abstractmethod

class AbstractMovementVisitor(ABC):

    @abstractmethod
    def visit_player(self):
        raise NotImplemented