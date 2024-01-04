from abc import ABC, abstractmethod

class AbstractTile(ABC):
    @abstractmethod
    def draw():
        raise NotImplemented
