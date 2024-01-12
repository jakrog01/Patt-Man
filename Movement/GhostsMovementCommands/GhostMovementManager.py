from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand

from Movement.GhostsMovementCommands.UpMovement import UpCommand
from Movement.GhostsMovementCommands.DownMovement import DownCommand
from Movement.GhostsMovementCommands.RightMovement import RightCommand
from Movement.GhostsMovementCommands.LeftMovement import LeftCommand


class GhostsMovementManager():
    def __init__(self, map, tile_size):
        self.__map = map
        self.__tile_size = tile_size
        
        self.__dict = {}
        self.add_move_direction("Up", UpCommand())
        self.add_move_direction("Down", DownCommand())
        self.add_move_direction("Right", RightCommand())
        self.add_move_direction("Left", LeftCommand())

    def add_move_direction(self, command:str, movement: AbstractGhostMovementCommand):
        self.__dict[command]= movement
        
    def move(self, character: str):
        if character.direction in self.__dict:
            self.__dict[character.direction](character, self.__map, self.__tile_size, character.speed)