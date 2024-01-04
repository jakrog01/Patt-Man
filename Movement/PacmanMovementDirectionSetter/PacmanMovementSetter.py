from Movement.PacmanMovementDirectionSetter.UpDirectionSetterCommand import UpDirectionSetterCommand
from Movement.PacmanMovementDirectionSetter.DownDirectionSetterCommand import DownDirectionSetterCommand
from Movement.PacmanMovementDirectionSetter.RightDirectionSetterCommand import RightDirectionSetterCommand
from Movement.PacmanMovementDirectionSetter.LeftDirectionSetterCommand import LeftDirectionSetterCommand
from Movement.PacmanMovementDirectionSetter.AbstractPacmanDirectionSetterCommand import AbstractPacmanDirectionSetterCommand

class PacmanMovementDirectionSetter():
    def __init__(self, pacman):
        self.__dict = {}
        
        self.add_direction_type("w", UpDirectionSetterCommand(pacman))
        self.add_direction_type("s", DownDirectionSetterCommand(pacman))
        self.add_direction_type("a", LeftDirectionSetterCommand(pacman))
        self.add_direction_type("d", RightDirectionSetterCommand(pacman))
    
    def add_direction_type(self, command:str, directionsetter: AbstractPacmanDirectionSetterCommand):
        self.__dict[command]= directionsetter
        
    def set_direction(self, command):
        if command in self.__dict:
            self.__dict[command]()