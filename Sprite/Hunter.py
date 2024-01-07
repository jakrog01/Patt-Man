import pygame
from Sprite.AbstractGhost import AbstractGhost
from Movement.GhostsStrategies.HunterStrategies.HunterNormalStrategy import HunterNormalStrategy
from Movement.GhostsStrategies.HunterStrategies.HunterDispersionStrategy import HunterDispersionStrategy

class Hunter(AbstractGhost):
    def __init__(self, x, y, tile_size, map):
        self.__x = x
        self.__y = y
        self.__strategy = HunterDispersionStrategy()
        self.__direction = "None"
        self.__tile_size = tile_size
        self.__map = map
        self.__score = 0

    def draw(self, win):
        pygame.draw.circle(win, "red", (self.__x, self.__y), int(self.__tile_size//2) + 5)

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, newx):
        self.__x = newx
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, newy):
        self.__y = newy

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, new_direction):
        self.__direction = new_direction

    @property
    def strategy(self):
        return self.__strategy
    
    def change_strategy(self):
        if isinstance(self.__strategy, HunterNormalStrategy):
            self.__strategy = HunterDispersionStrategy()

        elif isinstance(self.__strategy, HunterDispersionStrategy):
            self.__strategy = HunterNormalStrategy()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, newscore):
        self.__score = newscore

    def accept_director_changer_visitor(self, visitor):
        visitor.visitHunter(self)

    def accept_movement_visitor(self, visitor):
        visitor.visitHunter(self)