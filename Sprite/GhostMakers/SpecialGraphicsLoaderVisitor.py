from Sprite.Pacman import Pacman
from Sprite.AbstractGhost import AbstractGhost
import pygame

class SpecialGraphicLoaderVisitor():
    def __init__(self):
        self.__panic = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Panic.png"), (32, 32))

        self.__death = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Dead.png"), (32,32))

    def visit_ghost(self, ghost: AbstractGhost):
        ghost.load_grpahics(self.__panic, self.__death)