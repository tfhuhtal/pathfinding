import math
import heapq
import numpy as np

class JPS:
    """
    Jump Point Search algorithm
    """
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.operations = 0
        self.start = None
        self.goal = None


    def search(self, start, goal):
        self.start = start
        self.goal = goal

        previous = {}
        close_set = set()
        gscore = {self.start: 0}
        fscore = {self.start: self.heuristic(self.start, self.goal)}
        operations = 0
        queue = []

        heapq.heappush(queue, (fscore[self.start], self.start))

        while queue:
            operations += 1

            current = heapq.heappop(queue)[1]
            if current == self.goal:
                res = []
                while current in previous:
                    res.append(current)
                    current = previous[current]
                res.append(self.start)
                res = res[::-1]
                return (res, operations)

            close_set.add(current)

            successors = self.get_successors(
                current[0], current[1], previous
            )

            for successor in successors:
                jump_point = successor

                if jump_point in close_set:
                    continue

                tentative_g_score = gscore[current] + self.heuristic(current, jump_point)

                if (tentative_g_score < gscore.get(jump_point, 0)
                    or jump_point not in [j[1] for j in queue]):
                    previous[jump_point] = current
                    gscore[jump_point] = tentative_g_score
                    fscore[jump_point] = tentative_g_score + self.heuristic(jump_point, self.goal)
                    heapq.heappush(queue, (fscore[jump_point], jump_point))
        return (None, operations)

    #return jump points
    def jump(self, cur_x, cur_y, dir_x, dir_y):

        next_x = cur_x + dir_x
        next_y = cur_y + dir_y
        if self.blocked(next_x, next_y, 0, 0):
            return None

        if (next_x, next_y) == self.goal:
            return (next_x, next_y)

        temp_x = next_x
        temp_y = next_y

        if dir_x != 0 and dir_y != 0:
            while True:
                if (not self.blocked(temp_x, temp_y, -dir_x, dir_y)
                    and self.blocked(temp_x, temp_y, -dir_x, 0)
                    or not self.blocked(temp_x, temp_y, dir_x, -dir_y)
                    and self.blocked(temp_x, temp_y, 0, -dir_y)):
                    return (temp_x, temp_y)

                if (self.jump(temp_x, temp_y, dir_x, 0) is not None
                    or self.jump(temp_x, temp_y, 0, dir_y) is not None):
                    return (temp_x, temp_y)

                temp_x += dir_x
                temp_y += dir_y

                if self.blocked(temp_x, temp_y, 0, 0):
                    return None

                if (self.matrix[cur_x - dir_x][cur_y] == 1
                    and self.matrix[cur_x][cur_y - dir_y] == 1):
                    return None

                if (temp_x, temp_y) == self.goal:
                    return (temp_x, temp_y)
        else:
            if dir_x != 0:
                while True:
                    if (not self.blocked(temp_x, next_y, dir_x, 1)
                        and self.blocked(temp_x, next_y, 0, 1)
                        or not self.blocked(temp_x, next_y, dir_x, -1)
                        and self.blocked(temp_x, next_y, 0, -1)):
                        return (temp_x, next_y)

                    temp_x += dir_x

                    if self.blocked(temp_x, next_y, 0, 0):
                        return None

                    if (temp_x, next_y) == self.goal:
                        return (temp_x, next_y)

            else:
                while True:
                    if (not self.blocked(next_x, temp_y, 1, dir_y)
                        and self.blocked(next_x, temp_y, 1, 0)
                        or not self.blocked(next_x, temp_y, -1, dir_y)
                        and self.blocked(next_x, temp_y, -1, 0)):
                        return (next_x, temp_y)

                    temp_y += dir_y

                    if self.blocked(next_x, temp_y, 0, 0):
                        return None

                    if (next_x, temp_y) == self.goal:
                        return (next_x, temp_y)

        return self.jump(next_x, next_y, dir_x, dir_y)

    #return all possible neighbours of node
    def get_neighbours(self, cur_x, cur_y, parent):
        neighbours = []
        if parent == 0:
            for i, j in [(-1, 0),(0, -1),(1, 0),(0, 1),
                        (-1, -1),(-1, 1),(1, -1),(1, 1)]:
                if not self.blocked(cur_x, cur_y, i, j):
                    neighbours.append((cur_x + i, cur_y + j))

            return neighbours
        dir_x, dir_y = self.get_direction(cur_x, cur_y, parent[0], parent[1])

        if dir_x != 0 and dir_y != 0:
            if not self.blocked(cur_x, cur_y, 0, dir_y):
                neighbours.append((cur_x, cur_y + dir_y))
            if not self.blocked(cur_x, cur_y, dir_x, 0):
                neighbours.append((cur_x + dir_x, cur_y))
            if (not self.blocked(cur_x, cur_y, 0, dir_y)
                or not self.blocked(cur_x, cur_y, dir_x, 0))\
                and not self.blocked(cur_x, cur_y, dir_x, dir_y):
                neighbours.append((cur_x + dir_x, cur_y + dir_y))
            if self.blocked(cur_x, cur_y, -dir_x, 0)\
                and not self.blocked(cur_x, cur_y, 0, dir_y):
                neighbours.append((cur_x - dir_x, cur_y + dir_y))
            if self.blocked(cur_x, cur_y, 0, -dir_y)\
                and not self.blocked(cur_x, cur_y, dir_x, 0):
                neighbours.append((cur_x + dir_x, cur_y - dir_y))

        else:
            if dir_x == 0:
                if not self.blocked(cur_x, cur_y, dir_x, 0):
                    if not self.blocked(cur_x, cur_y, 0, dir_y):
                        neighbours.append((cur_x, cur_y + dir_y))
                    if self.blocked(cur_x, cur_y, 1, 0):
                        neighbours.append((cur_x + 1, cur_y + dir_y))
                    if self.blocked(cur_x, cur_y, -1, 0):
                        neighbours.append((cur_x - 1, cur_y + dir_y))

            else:
                if not self.blocked(cur_x, cur_y, dir_x, 0):
                    if not self.blocked(cur_x, cur_y, dir_x, 0):
                        neighbours.append((cur_x + dir_x, cur_y))
                    if self.blocked(cur_x, cur_y, 0, 1):
                        neighbours.append((cur_x + dir_x, cur_y + 1))
                    if self.blocked(cur_x, cur_y, 0, -1):
                        neighbours.append((cur_x + dir_x, cur_y - 1))
        return neighbours

    #return all possible successors of the current node
    def get_successors(self, cur_x, cur_y, previous):
        successors = []
        neighbours = self.get_neighbours(cur_x, cur_y, previous.get((cur_x, cur_y), 0))

        for node in neighbours:
            dir_x = node[0] - cur_x
            dir_y = node[1] - cur_y

            jump_point = self.jump(cur_x, cur_y, dir_x, dir_y)

            if jump_point is not None:
                successors.append(jump_point)

        return successors

    #check if the node is blocked, which means it is an obstacle or out of the map
    def blocked(self, cur_x, cur_y, dir_x, dir_y):
        max_x, max_y = self.matrix.shape
        next_x, next_y = cur_x + dir_x, cur_y + dir_y
        if not 0 <= next_x < max_x or not 0 <= next_y < max_y:
            return True
        if dir_x != 0 and dir_y != 0:
            if self.matrix[cur_x + dir_x, cur_y] == 1 and self.matrix[cur_x, cur_y + dir_y] == 1:
                return True
            if self.matrix[cur_x + dir_x, cur_y + dir_y] == 1:
                return True
        else:
            if dir_x != 0:
                if self.matrix[cur_x + dir_x, cur_y] == 1:
                    return True
            else:
                if self.matrix[cur_x, cur_y + dir_y] == 1:
                    return True
        return False

    #returns the direction of the jump
    def get_direction(self, cur_x, cur_y, point_x, point_y):
        dir_x = int(math.copysign(1, cur_x - point_x))
        dir_y = int(math.copysign(1, cur_y - point_y))
        if cur_x - point_x == 0:
            dir_x = 0
        if cur_y - point_y == 0:
            dir_y = 0
        return (dir_x, dir_y)


    def heuristic(self, node1, node2):
        return math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)
