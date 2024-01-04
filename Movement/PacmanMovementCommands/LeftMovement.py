from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class LeftCommand(AbstractPacmanMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, pacman, map, tile_size):
        y = int(pacman.y // tile_size)
        x = int(pacman.x // tile_size)
        
        if (pacman.x) % tile_size > 11:
                pacman.x = pacman.x - self.__speed
                
        elif pacman.x < 12:
            pacman.x = tile_size * len(map) - 12
        
        elif map[y][x-1] == 0 or map[y][x-1] == 9:
                pacman.x = pacman.x - self.__speed

        if map[y][x] == 9 and (pacman.x-3) % tile_size == 0:
            pacman.score = pacman.score + 10
            map[y][x] = 0