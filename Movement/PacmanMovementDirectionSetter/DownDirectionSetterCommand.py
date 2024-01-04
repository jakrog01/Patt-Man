from Movement.PacmanMovementDirectionSetter.AbstractPacmanDirectionSetterCommand import AbstractPacmanDirectionSetterCommand

class DownDirectionSetterCommand(AbstractPacmanDirectionSetterCommand):
    def __init__(self, pacman):
        self.__pacman = pacman

    def __call__(self):
        self.__pacman.next_direction = "Down"