from collections import deque

def get_next_move(map:list, ghost_x: int|float, ghost_y: int|float, respawn_x: int|float, respawn_y: int|float):
    rows = len(map)
    cols = len(map[0])

    visited = [[False] * cols for _ in range(rows)]
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    queue = deque([(ghost_x, ghost_y, [])])

    while queue:
        x, y, path = queue.popleft()
        visited[y][x] = True

        if x == respawn_x and y == respawn_y:
            return path[0] if path else "None"

        for move in moves:
            new_y = y + move[0]
            new_x = x + move[1]
            direction = move[2]

            if 0 <= y < rows and 0 <= x < cols and map[y][x] in {0, 7, 8, 9}:
                if not visited[new_y][new_x]:
                    new_path = path + [direction]
                    queue.append((new_x, new_y, new_path))
                    visited[new_y][new_x] = True
                    
    return "None"
