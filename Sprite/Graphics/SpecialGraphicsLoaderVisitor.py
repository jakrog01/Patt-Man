from Sprite.Pacman import Pacman
from Sprite.AbstractGhost import AbstractGhost
import pygame

class SpecialGraphicLoaderVisitor():
    def __init__(self):
        self.__panic = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Panic.png"), (32, 32))

        self.__death = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Dead.png"), (32,32))

        self.__one = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Pacman\\1.png"), (32,32))

        self.__two = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Pacman\\2.png"), (32,32))

        self.__three = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Pacman\\3.png"), (32,32))

        self.__four = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Pacman\\4.png"), (32,32))


    def visit_pacman(self, pacman: Pacman):
        pacman.load_graphics(self.__one, self.__two, self.__three, self.__four)

    def visit_ghost(self, ghost: AbstractGhost):
        ghost.load_grpahics(self.__panic, self.__death)