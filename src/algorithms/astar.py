import heapq
import math


class AStar:
    """
    A* algorithm
    """

    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        self.previous = [[None] * self.cols for _ in range(self.rows)]
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def search(self, start, end):
        self.distances[start[0]][start[1]] = 0
        self.previous[start[0]][start[1]] = start
        operations = 0

        heap = [(self.heuristic(start, end), start)]
        while heap:
            operations += 1
            current = heapq.heappop(heap)[1]
            if current == end:
                break
            if not self.visited[current[0]][current[1]]:
                self.visited[current[0]][current[1]] = True

            for direction in self.directions:
                neighbor = (
                    current[0] + direction[0],
                    current[1] + direction[1])
                if self.is_valid(neighbor):
                    if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        # Diagonal movement, distance is sqrt(2)
                        new_distance = self.distances[current[0]
                                                      ][current[1]] + math.sqrt(2)
                    else:
                        # Horizontal/Vertical movement, distance is 1
                        new_distance = self.distances[current[0]
                                                      ][current[1]] + 1

                    if new_distance < self.distances[neighbor[0]][neighbor[1]]:
                        self.distances[neighbor[0]][neighbor[1]] = new_distance
                        self.previous[neighbor[0]][neighbor[1]] = current
                        heapq.heappush(heap, (self.heuristic(neighbor, end)
                                              + new_distance, neighbor))

        return self.get_path(start, end, operations)

    # return heuristic value of node
    def heuristic(self, node, end):
        return math.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2)

    # return True if node is valid
    def is_valid(self, node):
        return (0 <= node[0] < self.rows
                and 0 <= node[1] < self.cols
                and not self.visited[node[0]][node[1]]
                and self.maze[node[0]][node[1]] == 0)

    # return path and number of operations
    def get_path(self, start, end, operations):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = self.previous[current[0]][current[1]]
        path.append(start)
        dist = self.distances[end[0]][end[1]]
        self.reset()
        return path[::-1], operations, dist

    # reset the algorithm
    def reset(self):
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        self.previous = [[None] * self.cols for _ in range(self.rows)]
