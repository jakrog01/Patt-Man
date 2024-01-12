from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand
from Sprite.AbstractGhost import AbstractGhost

class LeftCommand(AbstractGhostMovementCommand):
    def __call__(self, ghost: AbstractGhost, map: list, tile_size: int, speed: int|float):
        y = int(ghost.y // tile_size)
        x = int(ghost.x // tile_size)
        
        if (ghost.x) % tile_size > 11:
                ghost.x = ghost.x - speed

        elif map[y][x-1] == 0 or map[y][x-1] == 9 or map[y][x-1] == 8 or map[y][x-1] == 10:
                ghost.x = ghost.x - speed