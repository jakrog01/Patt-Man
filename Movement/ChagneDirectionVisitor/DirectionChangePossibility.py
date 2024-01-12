from Sprite.Player import Player

def check_direction_change_possibility(player: Player, map: list, tile_size: int) -> bool:

    x = int(player.x // tile_size)
    y = int(player.y // tile_size)
    
    if player.next_direction == "None":
        return False
    
    elif player.next_direction == "Up":
        if (player.x-11) % 21 != 0:
            return False 
        
        elif map[y-1][x] == 0 or map[y-1][x] == 9 or map[y-1][x] == 8 or map[y-1][x] == 10:
            return True
        
    elif player.next_direction == "Down":
        if (player.x-11) % 21 != 0:
            return False 
        
        elif map[y+1][x] == 0 or map[y+1][x] == 9 or map[y+1][x] == 8 or map[y+1][x] == 10:
            return True
    
    elif player.next_direction == "Left":
        if (player.y-11) % 21 != 0:
            return False 
        
        elif map[y][x-1] == 0 or map[y][x-1] == 9 or map[y][x-1] == 8 or map[y][x-1] == 10:
            return True
    
    elif player.next_direction == "Right":
        if (player.y-11) % 21 != 0:
            return False 
        
        elif map[y][x+1] == 0 or map[y][x+1] == 9 or map[y][x+1] == 8 or map[y][x+1] == 10: 
            return True
    
