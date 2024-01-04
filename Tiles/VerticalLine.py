from Tiles.TileAbstractClass import AbstractTile
import pygame

class VerticalTile(AbstractTile):
    def draw(self, win,i, j, color, size):
        pygame.draw.line(win, color, (j*size + int(size/2) , i*size), (j*size + int(size/2), i*size + size), 3)