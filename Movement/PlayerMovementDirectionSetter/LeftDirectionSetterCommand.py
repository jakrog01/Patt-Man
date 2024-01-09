from Movement.PlayerMovementDirectionSetter.AbstractPlayerDirectionSetterCommand import AbstractPlayerDirectionSetterCommand

class LeftDirectionSetterCommand(AbstractPlayerDirectionSetterCommand):
    def __init__(self, player):
        self.__player = player

    def __call__(self):
        self.__player.next_direction = "Left"