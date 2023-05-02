import math


class Dijkstra:
    """
    Algorithm:
    1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    2. Assign to every node a tentative distance value: set it to zero for our initial node
       and to infinity for all other nodes. Set the initial node as current.
    3. For the current node, consider all of its unvisited neighbors
       and calculate their tentative distances through the current node.
       Compare the newly calculated tentative distance
       to the current assigned value and assign the smaller one.
       For example, if the current node A is marked with a distance of 6,
       and the edge connecting it with a neighbor B has length 2,
       then the distance to B through A will be 6 + 2 = 8.
       If B was previously marked with a distance greater than 8
       then change it to 8. Otherwise, keep the current value.
    4. When we are done considering all of the neighbors of the current node,
       mark the current node as visited and remove it from the unvisited set.
       A visited node will never be checked again.
    5. If the destination node has been marked visited
       (when planning a route between two specific nodes)
       or if the smallest tentative distance among the nodes in
       the unvisited set is infinity (when planning a complete traversal;
       occurs when there is no connection between the initial node
       and remaining unvisited nodes), then stop. The algorithm has finished.
    6. Select the unvisited node that is marked with the smallest tentative distance,
       set it as the new "current node", and go back to step 3.
    Time Complexity: O(|V|^2)
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

        while True:
            operations += 1
            current = self.get_closest_node()
            if current is None:
                break
            self.visited[current[0]][current[1]] = True
            for direction in self.directions:
                neighbor = (
                    current[0] + direction[0],
                    current[1] + direction[1])
                if self.is_valid(neighbor):
                    if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        new_distance = self.distances[current[0]
                                                      ][current[1]] + math.sqrt(2)
                    else:
                        new_distance = self.distances[current[0]
                                                      ][current[1]] + 1
                    if new_distance < self.distances[neighbor[0]][neighbor[1]]:
                        self.distances[neighbor[0]][neighbor[1]] = new_distance
                        self.previous[neighbor[0]][neighbor[1]] = current

        return self.get_path(start, end, operations)

    def get_closest_node(self):
        min_distance = float('inf')
        closest_node = None
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.visited[i][j] and self.distances[i][j] < min_distance:
                    min_distance = self.distances[i][j]
                    closest_node = (i, j)
        return closest_node

    def is_valid(self, node):
        return (0 <= node[0] < self.rows
                and 0 <= node[1] < self.cols
                and not self.visited[node[0]][node[1]]
                and self.maze[node[0]][node[1]] == 0)

    def get_path(self, start, end, operations):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = self.previous[current[0]][current[1]]
        path.append(start)
        return path[::-1], operations
