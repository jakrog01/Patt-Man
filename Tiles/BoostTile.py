from Tiles.TileAbstractClass import AbstractTile
import pygame

class BoostTile(AbstractTile):
    def draw(self, win,i, j, color, size):
        pygame.draw.circle(win, color, (j*size+ int(size/2), i*size + int(size/2)), int(size // 3))