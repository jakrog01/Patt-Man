from Movement.PacmanMovementCommands.UpMovement import UpCommand
from Movement.PacmanMovementCommands.DownMovement import DownCommand
from Movement.PacmanMovementCommands.RightMovement import RightCommand
from Movement.PacmanMovementCommands.LeftMovement import LeftCommand
from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class PacmanMovementManager():
    def __init__(self, map, tile_size, ghosts):
        self.__map = map
        self.__tile_size = tile_size
        self.__ghosts = ghosts
        
        self.__dict = {}
        self.add_move_direction("Up", UpCommand(1))
        self.add_move_direction("Down", DownCommand(1))
        self.add_move_direction("Right", RightCommand(1))
        self.add_move_direction("Left", LeftCommand(1))
    
    def add_move_direction(self, command:str, movement: AbstractPacmanMovementCommand):
        self.__dict[command]= movement
        
    def move(self, character):
        if character.direction in self.__dict:
            self.__dict[character.direction](character, self.__map, self.__tile_size, self.__ghosts)