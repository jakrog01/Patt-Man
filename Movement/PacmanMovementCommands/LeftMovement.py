from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class LeftCommand(AbstractPacmanMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, pacman):
        pacman.x = pacman.x - self.__speed