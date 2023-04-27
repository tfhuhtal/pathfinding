import math
import heapq

def jps(start, goal, grid):

    def is_obstructed(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 1

    def has_forced_neighbour(x, y):
        # check for all possible neighbours of (x,y) whether they are forced
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            nx, ny = x + dx, y + dy
            if not is_obstructed(nx, ny) and (dx, dy) != (0, 0)\
                and (dx, dy) != (last_dir[x][y][0], last_dir[x][y][1]):
                if (nx, ny) == goal or \
                    is_obstructed(nx - last_dir[nx][ny][0], ny - last_dir[nx][ny][1]):
                    return True
        return False

    def direction(x, y):
        dx, dy = y[0] - x[0], y[1] - x[1]
        if dx > 0:
            if dy > 0:
                return (1, 1)
            elif dy < 0:
                return (1, -1)
            else:
                return (1, 0)
        elif dx < 0:
            if dy > 0:
                return (-1, 1)
            elif dy < 0:
                return (-1, -1)
            else:
                return (-1, 0)
        else:
            if dy > 0:
                return (0, 1)
            else:
                return (0, -1)

    def prune(x, neighbours):
        pruned = []
        last_dir[x[0]][x[1]] = (0, 0)
        for y in neighbours:
            di = direction(x, y)
            if di != last_dir[x[0]][x[1]]:
                if is_obstructed(x[0] + di[0], x[1] + di[1]):
                    continue
                if di[0] != 0 and di[1] != 0 and (is_obstructed(x[0], x[1] + di[1]) \
                    or is_obstructed(x[0] + di[0], x[1])):
                    continue
                pruned.append(y)
            last_dir[y[0]][y[1]] = di
        return pruned

    def jump(x, d, s, g):
        n = (x[0] + d[0], x[1] + d[1])
        if is_obstructed(n[0], n[1]):
            return None
        if n == g:
            return n
        if has_forced_neighbour(n[0], n[1]):
            return n
        if d in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for di in [(1,0),(0,1),(-1,0),(0,-1)]:
                if jump(n, di, s, g) is not None:
                    return n
        return jump(n, d, s, g)

    def neighbours(x):
        n = []
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x[0] + dx, x[1] + dy
            if not is_obstructed(nx, ny):
                n.append((nx, ny))
        return n

    def reconstruct_path(came_from, current, operations):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return operations, path[::-1]

    last_dir = [[(0, 0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
    start, goal = (start[0], start[1]), (goal[0], goal[1])

    f_score = {start: math.sqrt((start[0] - goal[0])**2 + (start[1] - goal[1])**2)}
    open_set = [(f_score[start], start)]
    came_from = {}
    g_score = {start: 0}
    operations = 0

    while open_set:
        operations += 1
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current, operations)
        for n in prune(current, neighbours(current)):
            g = g_score[current] + math.sqrt((n[0] - current[0])**2 + (n[1] - current[1])**2)
            if n not in g_score or g < g_score[n]:
                came_from[n] = current
                g_score[n] = g
                f_score[n] = g + math.sqrt((n[0] - goal[0])**2 + (n[1] - goal[1])**2)
                if n not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score[n], n))
    return None
