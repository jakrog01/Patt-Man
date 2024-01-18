from Tiles.TileAbstractClass import AbstractTile
import os
import pygame

class CherryTile(AbstractTile):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(os.path.join('Sprite','Graphics','Cherry.png')), (32,32))

    def draw(self, win, i: int, j: int, color: tuple, size: int):
        win.blit(self.__picture, ((i) *size, (j)* size - 5))