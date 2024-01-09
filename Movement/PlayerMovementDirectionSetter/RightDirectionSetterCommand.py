from Movement.PlayerMovementDirectionSetter.AbstractPlayerDirectionSetterCommand import AbstractPlayerDirectionSetterCommand

class RightDirectionSetterCommand(AbstractPlayerDirectionSetterCommand):
    def __init__(self, player):
        self.__player = player

    def __call__(self):
        self.__player.next_direction = "Right"