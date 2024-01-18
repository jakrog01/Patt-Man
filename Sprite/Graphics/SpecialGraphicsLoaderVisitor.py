from Sprite.Player import Player
from Sprite.AbstractGhost import AbstractGhost
import pygame
import os

class SpecialGraphicLoaderVisitor():
    def __init__(self):
        self.__panic = pygame.transform.scale(pygame.image.load( os.path.join("Sprite", "Graphics", "Panic.png")), (32, 32))

        self.__dead = pygame.transform.scale(pygame.image.load( os.path.join("Sprite", "Graphics", "Dead.png")), (32,32))

        self.__one = pygame.transform.scale(pygame.image.load(os.path.join('Sprite','Graphics','Player','1.png')), (32,32))

        self.__two = pygame.transform.scale(pygame.image.load(os.path.join('Sprite','Graphics','Player','2.png')), (32,32))

        self.__three = pygame.transform.scale(pygame.image.load(os.path.join('Sprite','Graphics','Player','3.png')), (32,32))

        self.__four = pygame.transform.scale(pygame.image.load(os.path.join('Sprite','Graphics','Player','4.png')), (32,32))

    def visit_player(self, pacman: Player):
        pacman.load_graphics(self.__one, self.__two, self.__three, self.__four)

    def visit_ghost(self, ghost: AbstractGhost):
        ghost.load_grpahics(self.__panic, self.__dead)