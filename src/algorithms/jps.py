import math
import heapq

class JPS:
    """
    Jump Point Search algorithm
    """
    def __init__(self, matrix):
        self.matrix = matrix
        self.distances = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        self.visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        self.previous = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        self.operations = 0

    def search(self, start, goal):
        self.distances[start[0]][start[1]] = 0
        self.previous[start[0]][start[1]] = start

        heap = [(self.heuristic(start, goal), start)]
        while heap:
            self.operations += 1
            
            current = heapq.heappop(heap)[1]
            if current == goal:
                return self.get_path(start, goal), self.operations, self.visited
            if not self.visited[current[0]][current[1]]:
                self.visited[current[0]][current[1]] = True
                neighbours = self.get_neighbours(current)

                for neighbour in neighbours:
                    direction = self.get_direction(current, neighbour)
                    jump_point = self.jump(neighbour, direction, goal)

                    if jump_point is None:
                        continue

                    old_distance = self.distances[jump_point[0]][jump_point[1]]
                    new_distance = self.distances[current[0]][current[1]] + self.get_jump_length(current, jump_point, direction)

                    if new_distance < old_distance:
                        self.distances[jump_point[0]][jump_point[1]] = new_distance
                        self.previous[jump_point[0]][jump_point[1]] = current
                        heapq.heappush(heap, (self.heuristic(jump_point, goal) + new_distance, jump_point))

        return None

    def jump(self, current, direction, goal):
        next_point =  (current[0] + direction[0], current[1] + direction[1])

        if not self.is_valid(next_point):
            return None

        if next_point == goal:
            return next_point

        y = next_point[0]
        x = next_point[1]

        if direction[0] == 0:
            if not self.is_valid((y + 1, current[0])) and self.is_valid((y + 1, x))\
            or not self.is_valid((y - 1, current[0])) and self.is_valid((y - 1, x)):
                return next_point
            
        elif direction[1] == 0:
            if not self.is_valid((current[0], x + 1)) and self.is_valid((y, x + 1))\
            or not self.is_valid((current[0], x - 1)) and self.is_valid((y, x - 1)):
                return next_point
            
        if direction[1] != 0 and direction[0] != 0:
            v_jump = self.jump(next_point, (0, direction[1]), goal)
            if v_jump is not None:
                return next_point
            
            h_jump = self.jump(next_point, (direction[0], 0), goal)
            if h_jump is not None:
                return next_point
            
        return self.jump(next_point, direction, goal)
    
    def get_neighbours(self, current):
        neighbours = []
        y, x = current

        prev = self.previous[y][x]

        if prev is not None or prev is None:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    neighbour_y, neighbour_x = y + dy, x + dx
                    if self.is_valid((neighbour_y, neighbour_x)):
                        neighbours.append((neighbour_y, neighbour_x))
                    else:
                        if dx == 0:
                            if self.is_valid((neighbour_y, neighbour_x + 1)):
                                neighbours.append((neighbour_y, neighbour_x + 1))
                            if self.is_valid((neighbour_y, neighbour_x - 1)):
                                neighbours.append((neighbour_y, neighbour_x - 1))
                        elif dy == 0:
                            if self.is_valid((neighbour_y + 1, neighbour_x)):
                                neighbours.append((neighbour_y + 1, neighbour_x))
                            if self.is_valid((neighbour_y - 1, neighbour_x)):
                                neighbours.append((neighbour_y - 1, neighbour_x))
            return neighbours
        
        direction = self.get_direction(prev, current)
        dy, dx = direction[0], direction[1]

        if dx == 0:
            if self.is_valid((y + dy, x)):
                neighbours.append((y + dy, x))
            if not self.is_valid((y - dy, x - 1)):
                if self.is_valid((y, x - 1)):
                    neighbours.append((y, x - 1))
                    if self.is_valid((y + dy, x)) and self.is_valid((y + dy, x - 1)):
                        neighbours.append((y + dy, x - 1))
            if not self.is_valid((y - dy, x + 1)):
                if self.is_valid((y, x + 1)):
                    neighbours.append((y, x + 1))
                    if self.is_valid((y + dy, x)) and self.is_valid((y + dy, x + 1)):
                        neighbours.append((y + dy, x + 1))
        elif dy == 0:
            if self.is_valid((y, x + dx)):
                neighbours.append((y, x + dx))
            if not self.is_valid((y - 1, x - dx)):
                if self.is_valid((y - 1, x)):
                    neighbours.append((y - 1, x))
                    if self.is_valid((y, x + dx)) and self.is_valid((y - 1, x + dx)):
                        neighbours.append((y - 1, x + dx))
            if not self.is_valid((y + 1, x - dx)):
                if self.is_valid((y + 1, x)):
                    neighbours.append((y + 1, x))
                    if self.is_valid((y, x + dx)) and self.is_valid((y + 1, x + dx)):
                        neighbours.append((y + 1, x + dx))
        else:
            if self.is_valid((y + dy, x + dx)):
                neighbours.append((y + dy, x + dx))
            if not self.is_valid((y, x + dx)):
                if self.is_valid((y - dy, x)):
                    neighbours.append((y - dy, x))
                    if self.is_valid((y - dy, x + dx)) and self.is_valid((y - dy, x)):
                        neighbours.append((y - dy, x + dx))
                if self.is_valid((y + dy, x)):
                    neighbours.append((y + dy, x))
                    if self.is_valid((y + dy, x + dx)) and self.is_valid((y + dy, x)):
                        neighbours.append((y + dy, x + dx))

        return neighbours


    def get_direction(self, current, neighbour):
        return (neighbour[0] - current[0], neighbour[1] - current[1])
    
    def get_distance(self, current, neighbour):
        return math.sqrt((current[0] - neighbour[0])**2 + (current[1] - neighbour[1])**2)
    
    def is_valid(self, point):
        return 0 <= point[0] < len(self.matrix) and 0 <= point[1] < len(self.matrix[0]) and self.matrix[point[0]][point[1]] == 0

    def heuristic(self, current, goal):
        return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)
    
    def get_path(self, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = self.previous[current[0]][current[1]]
        path.append(start)
        return path[::-1]

    def get_jump_length(self, current, neighbour, direction):
        x = current[0] - neighbour[0]
        y = current[1] - neighbour[1]

        if x < 0:
            x = -x

        if y < 0:
            y = -y

        if direction[0] == 0 or direction[1] == 0:
            return x + y
        else:
            return x * (2)**0.5
