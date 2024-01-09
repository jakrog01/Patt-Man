def check_direction_change_possibility(pacman, map, tile_size):

    x = int(pacman.x // tile_size)
    y = int(pacman.y // tile_size)
    
    if pacman.next_direction == "None":
        return False
    
    elif pacman.next_direction == "Up":
        if (pacman.x-11) % 21 != 0:
            return False 
        
        elif map[y-1][x] == 0 or map[y-1][x] == 9 or map[y-1][x] == 8:
            return True
        
    elif pacman.next_direction == "Down":
        if (pacman.x-11) % 21 != 0:
            return False 
        
        elif map[y+1][x] == 0 or map[y+1][x] == 9 or map[y+1][x] == 8:
            return True
    
    elif pacman.next_direction == "Left":
        if (pacman.y-11) % 21 != 0:
            return False 
        
        elif map[y][x-1] == 0 or map[y][x-1] == 9 or map[y][x-1] == 8:
            return True
    
    elif pacman.next_direction == "Right":
        if (pacman.y-11) % 21 != 0:
            return False 
        
        elif map[y][x+1] == 0 or map[y][x+1] == 9 or map[y][x+1] == 8: 
            return True
    
