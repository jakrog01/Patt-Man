from Tiles.TileAbstractClass import AbstractTile
import pygame

class RightDownPerpendicularTile(AbstractTile):
    def draw(self, win,i, j, color, size):
        pygame.draw.line(win, color, (j*size + int(size/2), i*size + int(size/2)), (j*size + size, i*size + int(size/2)), 3)
        pygame.draw.line(win, color, (j*size + int(size/2) , i*size + int(size/2)), (j*size + int(size/2), i*size + size), 3)