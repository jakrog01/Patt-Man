from abc import ABC

class AbstractGhostMovementCommand(ABC):
    def __call__(self):
        raise NotImplemented