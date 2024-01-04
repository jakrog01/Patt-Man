from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class DownCommand(AbstractPacmanMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, pacman):
        pacman.y = pacman.y + self.__speed