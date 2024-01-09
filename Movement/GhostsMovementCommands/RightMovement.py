from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand

class RightCommand(AbstractGhostMovementCommand):
    def __call__(self, ghost, map, tile_size, speed):
        y = int(ghost.y // tile_size)
        x = int(ghost.x // tile_size)

        if ghost.x % tile_size < 11:
            ghost.x = ghost.x + speed    

        elif map[y][x+1] == 0 or map[y][x+1] == 9 or map[y][x+1] == 8:
            ghost.x = ghost.x + speed