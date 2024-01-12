from abc import ABC

class AbstractPlayerMovementCommand(ABC):
    def __init__(self):
        raise NotImplemented
    
    def __call__(self):
        raise NotImplemented