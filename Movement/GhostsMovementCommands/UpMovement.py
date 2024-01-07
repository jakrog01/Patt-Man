from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand

class UpCommand(AbstractGhostMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, ghost, map, tile_size):
        y = int(ghost.y // tile_size)
        x = int(ghost.x // tile_size)
        
        if (ghost.y) % tile_size > 11:
                ghost.y = ghost.y - self.__speed

        elif map[y-1][x] == 0 or map[y-1][x] == 9 or map[y-1][x] == 7:
                ghost.y = ghost.y - self.__speed