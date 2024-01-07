from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class TraperNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, hunter, pacman, tile_size, map):
        allowed_directions = []

        hunter_x = int(hunter.x // tile_size)
        hunter_y = int(hunter.y // tile_size)

        destination_x = int(pacman.x // tile_size)
        destination_y = int(pacman.y // tile_size)

        if pacman.direction == "Up":
            destination_y -= 4
        elif pacman.direction == "Down":
            destination_y += 4
        elif pacman.direction == "Right":
            destination_x += 4
        elif pacman.direction == "Left":
            destination_x -= 4

        distance = 1000000
        new_direction = "None"

        if hunter.direction != "Left":
            if map[hunter_y][hunter_x+1] == 9 or map[hunter_y][hunter_x+1] == 0:
                new_distance = ((hunter_x+1) - destination_x)**2 + (hunter_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if hunter.direction != "Right":
            if map[hunter_y][hunter_x-1] == 9 or map[hunter_y][hunter_x-1] == 0:
                new_distance = ((hunter_x-1) - destination_x)**2 + (hunter_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if hunter.direction != "Up":
            if map[hunter_y+1][hunter_x] == 9 or map[hunter_y+1][hunter_x] == 0:
                new_distance = (hunter_x - destination_x)**2 + ((hunter_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if hunter.direction != "Down":
            if map[hunter_y-1][hunter_x] == 9 or map[hunter_y-1][hunter_x] == 0 or map[hunter_y-1][hunter_x] == 7:
                new_distance = (hunter_x - destination_x)**2 + ((hunter_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        hunter.direction = new_direction

        if new_direction == "None":
            hunter.direction = hunter.direction = "Right"
        
            