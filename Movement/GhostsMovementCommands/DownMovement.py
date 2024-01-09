from Movement.GhostsMovementCommands.AbstractGhostMovementCommand import AbstractGhostMovementCommand

class DownCommand(AbstractGhostMovementCommand):
    def __call__(self, ghost, map, tile_size, speed):
        y = int(ghost.y // tile_size)
        x = int(ghost.x // tile_size)
        
        if (ghost.y) % tile_size < 11:
                ghost.y = ghost.y + speed

        elif map[y+1][x] == 0 or map[y+1][x] == 9 or map[y+1][x] == 8:
                ghost.y = ghost.y + speed
        
        elif ghost.picture == ghost.dead_picture:
            if map[y+1][x] == 0 or map[y+1][x] == 9 or map[y+1][x] == 8 or map[y+1][x] == 7:
                ghost.y = ghost.y + speed