from abc import ABC

class AbstractPlayerDirectionSetterCommand(ABC):    
    def __call__(self):
        raise NotImplemented