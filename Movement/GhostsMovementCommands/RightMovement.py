from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand

class RightCommand(AbstractGhostMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, ghost, map, tile_size):
        y = int(ghost.y // tile_size)
        x = int(ghost.x // tile_size)

        if ghost.x % tile_size < 11:
            ghost.x = ghost.x + self.__speed

        elif ghost.x > tile_size * len(map) - 11:
            ghost.x = 5       

        elif map[y][x+1] == 0 or map[y][x+1] == 9:
            ghost.x = ghost.x + self.__speed