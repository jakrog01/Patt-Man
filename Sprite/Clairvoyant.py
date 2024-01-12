import pygame
from Sprite.AbstractGhost import AbstractGhost

from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy
from Movement.AbstractMovementVisitor import AbstractMovementVisitor

from Movement.GhostsStrategies.ClairvoyantStrategies.ClairvoyantNormalStrategy import ClairvoyantNormalStrategy
from Movement.GhostsStrategies.GhostHouseStrategy import GhostHouseStrategy
from Movement.GhostsStrategies.GhostPanicStrategy import GhostPanicStrategy
from Movement.GhostsStrategies.GhostRespawnStrategy import GhostRespawnStrategy


class Clairvoyant(AbstractGhost):
    def __init__(self, x: int, y: int, respawn_point: tuple, tile_size: int, map: list, picture: pygame.image):
        self.__x = x
        self.__y = y
        self.__respawn_y = respawn_point[0]
        self.__respawn_x = respawn_point[1]
        
        self.__strategy = GhostHouseStrategy()
        self.__direction = "Right"
        self.__tile_size = tile_size
        self.__map = map
        self.__score = 0

        self.__normal_picture = picture
        self.__dead_picture = None
        self.__panic_picture = None
        self.__picture = self.__normal_picture

        self.__state = "Home"
        self.__inverter = {"Left": "Right", "Right": "Left", "Up": "Down", "Down":"Up"}
        self.__speed = 1

    def draw(self, win: pygame.surface):
        flip = (False, False)
        if self.direction == "Left":
            flip = (True, False)
        
        fliped_image = pygame.transform.flip(self.__picture, flip[0], flip[1])

        win.blit(fliped_image, (self.__x - 16, self.__y-16))
    
    def load_grpahics(self, panic: pygame.image, dead: pygame.image):
        self.__panic_picture = panic
        self.__dead_picture = dead

    def inverse_direction(self):
        self.__direction = self.__inverter[self.__direction]
    
    def enter_prey_mode(self):
        self.inverse_direction()
        self.__strategy = GhostPanicStrategy()
        self.__picture = self.__panic_picture
        self.__state = "Prey"
        self.__speed = 0.5

    def enter_predator_mode(self):
        self.__x = round(self.__x)
        self.__y = round(self.__y)

        if self.state == "Prey":
            self.inverse_direction()

        self.__strategy = ClairvoyantNormalStrategy()
        self.__picture = self.__normal_picture
        self.__state = "Predator"
        self.__speed = 1

    def enter_dead_mode(self):
        self.__x = round(self.__x)
        self.__y = round(self.__y)

        self.__strategy = GhostRespawnStrategy()
        self.__picture = self.__dead_picture
        self.__state = "Dead"
        self.__speed = 1

    @property
    def respawn_x(self):
        return self.__respawn_x
    @property
    def respawn_y(self):
        return self.__respawn_y
    
    @property
    def picture(self):
        return self.__picture
    
    @property
    def dead_picture(self):
        return self.__dead_picture
    
    @property
    def normal_picture(self):
        return self.__normal_picture
    
    @property
    def panic_picture(self):
        return self.__panic_picture
    
    @picture.setter
    def picture(self, new_picture: pygame.image):
        self.__picture = new_picture

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x: int|float):
        self.__x = new_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y: int|float):
        self.__y = new_y

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, new_direction: str):
        self.__direction = new_direction

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy: AbstractGhostStrategy):
        self.__strategy = new_strategy

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score: int):
        self.__score = new_score

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new_state: str):
        self.__state = new_state

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, new_speed: int|float):
        self.__speed = new_speed
    
    def accept_director_changer_visitor(self, visitor: AbstractMovementVisitor):
        visitor.visit_clairvoyant(self)

    def accept_movement_visitor(self, visitor: AbstractMovementVisitor):
        visitor.visit_ghost(self)
    
    def accept_graphic_loader_visitor(self, visitor: AbstractMovementVisitor):
        visitor.visit_ghost(self)