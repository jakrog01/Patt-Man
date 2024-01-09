from Tiles.TileAbstractClass import AbstractTile
import pygame

class CherryTile(AbstractTile):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Cherry.png"), (32,32))

    def draw(self, win, i: int, j: int, color: tuple, size: int):
        win.blit(self.__picture, ((i) *size, (j)* size - 5))