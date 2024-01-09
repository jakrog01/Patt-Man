from Tiles.HorizontalTile import HorizontalTile
from Tiles.VerticalLine import VerticalTile
from Tiles.TileDispatch import TileDispatch
from Tiles.RightDownPerpendicularTile import RightDownPerpendicularTile
from Tiles.LeftDownPerpendicularTile import LeftDownPerpendicularTile
from Tiles.LeftUpPerpendicularTile import LeftUpPerpendicularTile
from Tiles.RightUpPerpendicularTile import RightUpPerpendicularTile
from Tiles.BoostTile import BoostTile
from Tiles.PointTile import PointTile
from Tiles.BarierTile import BarierTile

from Movement.GhostsStrategies.GhostDispersionStrategy import GhostDispersionStrategy

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
        self.__tile_drawer.add_tile_type(8, BoostTile())
        self.__tile_drawer.add_tile_type(9, PointTile())
    
    def draw_map(self, win):
        for i in range(30):
            for j in range(30):
                self.__tile_drawer.draw_tile(win, self.__map[i][j], i, j)

    @staticmethod
    def check_collisions(pacman, list, tile_size):
        if pacman.state == "Predator":
            pacman.counter = pacman.counter + 1

        x = int(pacman.x // tile_size)
        y = int(pacman.y // tile_size)

        for ghost in list:
            ghost_x = (ghost.x // tile_size)
            ghost_y = (ghost.y // tile_size)

            if ghost_x == x and ghost_y == y and ghost.state == "Predator":
                return True
            elif ghost_x == x and ghost_y == y and ghost.state == "Prey":
                ghost.enter_dead_mode()
                pacman.kill_streak = pacman.kill_streak + 1
                pacman.score = pacman.score + pacman.kill_streak * 200
        return False
    
    @staticmethod
    def place_in_starting_positions(pacman, ghost_list, tile_size, position_list):
        pacman.y = int((position_list[0][0]-1) * tile_size) + 11
        pacman.x = int((position_list[0][1]-1) * tile_size) + 11

        for index, ghost in enumerate(ghost_list):
            ghost.y = int((position_list[index+1][0] - 1) * tile_size) + 11
            ghost.x = int((position_list[index+1][1] -1) * tile_size) + 11

            if ghost.state != "Home":
                ghost.enter_predator_mode()

