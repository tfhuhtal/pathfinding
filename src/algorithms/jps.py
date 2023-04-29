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

        heap = [(self.heuristic(start, goal), start)]
        while heap:
            self.operations += 1
            print(heap)
            current = heapq.heappop(heap)[1]
            if current == goal:
                return self.get_path(start, goal), self.operations, self.visited
            successors = self.get_successors(current, goal)
            for successor in successors:
                if not self.visited[successor[0]][successor[1]]:
                    self.visited[successor[0]][successor[1]] = True
                    self.previous[successor[0]][successor[1]] = current
                    self.distances[successor[0]][successor[1]] = self.distances[current[0]][current[1]] + 1
                    heapq.heappush(heap, (self.heuristic(successor, goal), successor))

        return None, None, None

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
        prev = self.previous[current[0]][current[1]]
        if prev is None:
            for i, j in [(-1, 0),(0, -1),(1, 0),(0, 1),(-1, -1),(-1, 1),(1, -1),(1, 1)]:
                if self.is_valid((current[0] + i, current[1] + j)):
                    neighbours.append((current[0] + i, current[1] + j)) 
            return neighbours
        
        cur_y, cur_x = current

        dir_y, dir_x = self.get_direction(prev, current)

        if dir_x == 0:
            if self.is_valid((cur_y + dir_y, cur_x)):
                neighbours.append((cur_y + dir_y, cur_x))
            if not self.is_valid((cur_y - dir_y, cur_x - 1)):
                if self.is_valid((cur_y, cur_x - 1)):
                    neighbours.append((cur_y, cur_x - 1))
                    if self.is_valid((cur_y + dir_y, cur_x)) and self.is_valid((cur_y + dir_y, cur_x - 1)):
                        neighbours.append((cur_y + dir_y, cur_x - 1))
            if not self.is_valid((cur_y - dir_y, cur_x + 1)):
                if self.is_valid((cur_y, cur_x + 1)):
                    neighbours.append((cur_y, cur_x + 1))
                    if self.is_valid((cur_y + dir_y, cur_x)) and self.is_valid((cur_y + dir_y, cur_x + 1)):
                        neighbours.append((cur_y + dir_y, cur_x + 1))

        elif dir_y == 0:
            if self.is_valid((cur_y, cur_x + dir_x)):
                neighbours.append((cur_y, cur_x + dir_x))
            if not self.is_valid((cur_y - 1, cur_x - dir_x)):
                if self.is_valid((cur_y - 1, cur_x)):
                    neighbours.append((cur_y - 1, cur_x))
                    if self.is_valid((cur_y, cur_x + dir_x)) and self.is_valid((cur_y - 1, cur_x + dir_x)):
                        neighbours.append((cur_y - 1, cur_x + dir_x))
            if not self.is_valid((cur_y + 1, cur_x - dir_x)):
                if self.is_valid((cur_y + 1, cur_x)):
                    neighbours.append((cur_y + 1, cur_x))
                    if self.is_valid((cur_y, cur_x + dir_x)) and self.is_valid((cur_y + 1, cur_x + dir_x)):
                        neighbours.append((cur_y + 1, cur_x + dir_x))

        else:
            if self.is_valid((cur_y + dir_y, cur_x)):
                neighbours.append((cur_y + dir_y, cur_x))
            if self.is_valid((cur_y, cur_x + dir_x)):
                neighbours.append((cur_y, cur_x + dir_x))
            if self.is_valid((cur_y + dir_y, cur_x)) and self.is_valid((cur_y, cur_x + dir_x)):
                if self.is_valid((cur_y + dir_y, cur_x + dir_x)):
                    neighbours.append((cur_y + dir_y, cur_x + dir_x))

        return neighbours

    def get_successors(self, current, goal):
        successors = []
        neighbours = self.get_neighbours(current)
        for node in neighbours:
            jump_point = self.jump(current, node, goal)
            
            if jump_point is not None:
                successors.append(jump_point)

        return successors

    def get_direction(self, prev, curr):
        dir_y = int(math.copysign(1, curr[0] - prev[0]))
        dir_x = int(math.copysign(1, curr[1] - prev[1]))
        if prev[0] == curr[0]:
            dir_y = 0
        if prev[1] == curr[1]:
            dir_x = 0
        return (dir_y, dir_x)

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
