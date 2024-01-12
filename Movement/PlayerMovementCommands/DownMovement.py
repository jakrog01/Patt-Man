from Movement.PlayerMovementCommands.AbstractPlayerMovementCommand import AbstractPlayerMovementCommand
from Sprite.Player import Player

class DownCommand(AbstractPlayerMovementCommand):
    def __init__(self, speed: int|float):
        self.__speed = speed
    
    def __call__(self, player: Player, map: list, tile_size: int, ghosts: list):
        y = int(player.y // tile_size)
        x = int(player.x // tile_size)
        
        if (player.y) % tile_size < 11:
                player.y = player.y + self.__speed

        elif map[y+1][x] == 0 or map[y+1][x] == 9 or map[y+1][x] == 8 or map[y+1][x] == 10:
                player.y = player.y + self.__speed

        if map[y][x] == 9 and (player.y - 20) % tile_size == 0:
            player.score = player.score + 10
            map[y][x] = 0
        
        elif map[y][x] == 10 and (player.y - 7) % tile_size == 0:
            player.score = player.score + 1000
            map[y][x] = 0

        elif map[y][x] == 8 and (player.y-7) % tile_size == 0:
            player.score = player.score + 50
            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.enter_prey_mode()

            player.enter_predator_mode()
            map[y][x] = 0
        