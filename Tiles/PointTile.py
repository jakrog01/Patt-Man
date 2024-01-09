from Tiles.TileAbstractClass import AbstractTile
import pygame

class PointTile(AbstractTile):
    def draw(self, win, i: int, j: int, color: tuple, size: int):
        pygame.draw.circle(win, color, (j*size+ int(size/2), i*size + int(size/2)), int(size // 7))