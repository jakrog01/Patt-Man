from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class TraperNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, traper, pacman, tile_size, map, *args):

        traper_x = int(traper.x // tile_size)
        traper_y = int(traper.y // tile_size)

        hunter_x = int(traper.hunter.x // tile_size)
        hunter_y = int(traper.hunter.y // tile_size)

        pacman_x = int(pacman.x // tile_size)
        pacman_y = int(pacman.y // tile_size)

        if pacman.direction == "Up":
            pacman_y -= 2
        elif pacman.direction == "Down":
            pacman_y += 2
        elif pacman.direction == "Right":
            pacman_x += 2
        elif pacman.direction == "Left":
            pacman_x -= 2

        x_diff = pacman_x - hunter_x
        y_diff = pacman_y - hunter_y

        destination_x = hunter_x + 2*x_diff
        destination_y = hunter_y + 2*y_diff

        distance = 1000000
        new_direction = "None"

        if traper.direction != "Left":
            if map[traper_y][traper_x+1] == 9 or map[traper_y][traper_x+1] == 0 or map[traper_y][traper_x+1] == 8  or map[traper_y][traper_x+1] == 10:
                new_distance = ((traper_x+1) - destination_x)**2 + (traper_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if traper.direction != "Right":
            if map[traper_y][traper_x-1] == 9 or map[traper_y][traper_x-1] == 0 or map[traper_y][traper_x-1] == 8 or map[traper_y][traper_x-1] == 10:
                new_distance = ((traper_x-1) - destination_x)**2 + (traper_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if traper.direction != "Up":
            if map[traper_y+1][traper_x] == 9 or map[traper_y+1][traper_x] == 0 or map[traper_y+1][traper_x] == 8 or map[traper_y+1][traper_x] == 10:
                new_distance = (traper_x - destination_x)**2 + ((traper_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if traper.direction != "Down":
            if map[traper_y-1][traper_x] == 9 or map[traper_y-1][traper_x] == 0 or map[traper_y-1][traper_x] == 7 or map[traper_y-1][traper_x] == 8 or map[traper_y-1][traper_x] == 10:
                new_distance = (traper_x - destination_x)**2 + ((traper_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
            traper.inverse_direction()
        else:
            traper.direction = new_direction
        
            