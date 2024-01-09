from Tiles.TileAbstractClass import AbstractTile

class TileDispatch():
    def __init__(self, size: int, color: tuple):
        self.__dict = {}
        self.__tile_size= size
        self.__color = color
    
    def add_tile_type(self, command: str, tile: AbstractTile):
        self.__dict[command]= tile
        
    def draw_tile(self, win, command: str, i: int, j: int):
        if command in self.__dict:
            self.__dict[command].draw(win,i, j, self.__color, self.__tile_size)