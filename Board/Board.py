from Tiles.HorizontalTile import HorizontalTile
from Tiles.VerticalLine import VerticalTile
from Tiles.TileDispatch import TileDispatch
from Tiles.RightDownPerpendicularTile import RightDownPerpendicularTile
from Tiles.LeftDownPerpendicularTile import LeftDownPerpendicularTile
from Tiles.LeftUpPerpendicularTile import LeftUpPerpendicularTile
from Tiles.RightUpPerpendicularTile import RightUpPerpendicularTile
from Tiles.PointTile import PointTile
from Tiles.BarierTile import BarierTile

class Board():
    def __init__(self, map, tile_size) -> None:
        self.__map = map
        
        self.__tile_drawer = TileDispatch(tile_size, (255,255,255))
        self.__tile_drawer.add_tile_type(1, HorizontalTile())
        self.__tile_drawer.add_tile_type(2, VerticalTile())
        self.__tile_drawer.add_tile_type(3, RightDownPerpendicularTile())
        self.__tile_drawer.add_tile_type(4, LeftDownPerpendicularTile())
        self.__tile_drawer.add_tile_type(5, RightUpPerpendicularTile())
        self.__tile_drawer.add_tile_type(6, LeftUpPerpendicularTile())
        self.__tile_drawer.add_tile_type(7, BarierTile())
        self.__tile_drawer.add_tile_type(9, PointTile())
    
    def draw_map(self, win):
        for i in range(30):
            for j in range(30):
                self.__tile_drawer.draw_tile(win, self.__map[i][j], i, j)

    @staticmethod
    def check_collisions(pacman, list, tile_size):
        x = int(pacman.x // tile_size)
        y = int(pacman.y // tile_size)

        for element in list:
            ghost_x = (element.x // tile_size)
            ghost_y = (element.y // tile_size)

            if ghost_x == x and ghost_y == y:
                return True
            
        return False
            

