from Movement.PlayerMovementDirectionSetter.UpDirectionSetterCommand import UpDirectionSetterCommand
from Movement.PlayerMovementDirectionSetter.DownDirectionSetterCommand import DownDirectionSetterCommand
from Movement.PlayerMovementDirectionSetter.RightDirectionSetterCommand import RightDirectionSetterCommand
from Movement.PlayerMovementDirectionSetter.LeftDirectionSetterCommand import LeftDirectionSetterCommand
from Movement.PlayerMovementDirectionSetter.AbstractPlayerDirectionSetterCommand import AbstractPlayerDirectionSetterCommand
from Sprite.Player import Player

class PlayerMovementDirectionSetter():
    def __init__(self, player: Player):
        self.__dict = {}
        
        self.add_direction_type("w", UpDirectionSetterCommand(player))
        self.add_direction_type("s", DownDirectionSetterCommand(player))
        self.add_direction_type("a", LeftDirectionSetterCommand(player))
        self.add_direction_type("d", RightDirectionSetterCommand(player))
    
    def add_direction_type(self, command:str, directionsetter: AbstractPlayerDirectionSetterCommand):
        self.__dict[command]= directionsetter
        
    def set_direction(self, command: str):
        if command in self.__dict:
            self.__dict[command]()