from Movement.PlayerMovementCommands.UpMovement import UpCommand
from Movement.PlayerMovementCommands.DownMovement import DownCommand
from Movement.PlayerMovementCommands.RightMovement import RightCommand
from Movement.PlayerMovementCommands.LeftMovement import LeftCommand
from Movement.PlayerMovementCommands.AbstractPlayerMovementCommand import AbstractPlayerMovementCommand

class PlayerMovementManager():
    def __init__(self, map, tile_size, ghosts):
        self.__map = map
        self.__tile_size = tile_size
        self.__ghosts = ghosts
        
        self.__dict = {}
        self.add_move_direction("Up", UpCommand(1))
        self.add_move_direction("Down", DownCommand(1))
        self.add_move_direction("Right", RightCommand(1))
        self.add_move_direction("Left", LeftCommand(1))
    
    def add_move_direction(self, command:str, movement: AbstractPlayerMovementCommand):
        self.__dict[command]= movement
        
    def move(self, character):
        if character.direction in self.__dict:
            self.__dict[character.direction](character, self.__map, self.__tile_size, self.__ghosts)