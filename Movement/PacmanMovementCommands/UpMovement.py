from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class UpCommand(AbstractPacmanMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, pacman, map, tile_size):
        y = int(pacman.y // tile_size)
        x = int(pacman.x // tile_size)
        
        if (pacman.y) % tile_size > 11:
                pacman.y = pacman.y - self.__speed

        elif map[y-1][x] == 0 or map[y-1][x] == 9:
                pacman.y = pacman.y - self.__speed

        if map[y][x] == 9 and (pacman.y + 7) % tile_size == 0:
            pacman.score = pacman.score + 10
            map[y][x] = 0