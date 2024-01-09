from Tiles.TileAbstractClass import AbstractTile
import pygame

class BarierTile(AbstractTile):
    def draw(self, win: pygame.surface, i: int, j: int, color: tuple, size: int):
        pygame.draw.line(win, (255,0,0), (j*size - int(size/2) + 2, i*size + int(size/2)), (j*size + size + int(size/2) -2 , i*size + int(size/2)), 3)