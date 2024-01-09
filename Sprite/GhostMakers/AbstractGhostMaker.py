from abc import ABC, abstractmethod

class AbstractGhostMaker(ABC):
    @abstractmethod
    def make(self, *args):
        raise NotImplemented