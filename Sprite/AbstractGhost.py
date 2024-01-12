from abc import ABC, abstractmethod

class AbstractGhost(ABC):

    def __init__(self, x ,y):
        self.__x = x
        self.__y = y
        
    @abstractmethod
    def draw(self):
        raise NotImplemented
    
    @abstractmethod
    def load_grpahics(self):
        raise NotImplemented
    
    @abstractmethod
    def inverse_direction(self):
        raise NotImplemented
    
    @abstractmethod
    def enter_prey_mode(self):
        raise NotImplemented
    
    @abstractmethod
    def enter_predator_mode(self):
        raise NotImplemented
    
    @abstractmethod
    def enter_dead_mode(self):
        raise NotImplemented
    
    @abstractmethod
    def accept_director_changer_visitor(self):
        raise NotImplemented

    @abstractmethod
    def accept_movement_visitor(self):
        raise NotImplemented
    
    @abstractmethod
    def accept_graphic_loader_visitor(self):
        raise NotImplemented