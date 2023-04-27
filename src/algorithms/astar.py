import heapq
import math

class AStar:
    """
    Algorithm:
    1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

    2. Assign to every node a tentative distance value: set it to zero for our initial node and to
    infinity for all other nodes. Also, calculate a heuristic function h(n) for each node n, which
    estimates the distance from node n to the goal node. Set the initial node as current.

    3. For the current node, consider all of its unvisited neighbors and calculate their tentative
    distances through the current node. Add the heuristic value of each neighbor to the tentative
    distance to create a new value called f(n) for each neighbor n. Compare the newly calculated
    f(n) value to the current assigned f(n) value and assign the smaller one. For example, if the
    current node A is marked with a distance of 6 and the edge connecting it with a neighbor B has
    length 2, and the heuristic function h(B) returns 3, then the f value of B through A will be
    6 + 2 + 3 = 11. If B was previously marked with a f value greater than 11, then change it to 11.
    Otherwise, keep the current value.

    4. When we are done considering all of the neighbors of the current node, mark the current node
    as visited and remove it from the unvisited set. A visited node will never be checked again.

    5. If the destination node has been visited (when planning a route between two specific nodes)
    or if the smallest tentative f value among the nodes in the unvisited set is infinity
    (when planning a complete traversal),then stop. The algorithm has finished. 

    6. Otherwise, select the unvisited node that is marked with the smallest tentative f value,
    and set it as the new "current node" then go back to step 3.

    The algorithm will terminate when either the goal node has been visited or there are no more
    nodes left to visit in the unvisited set. The resulting path can be reconstructed by starting
    at the goal node and following the path of nodes with the lowest tentative f value back to the
    initial node.
    """

    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        self.previous = [[None] * self.cols for _ in range(self.rows)]
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.operations = 0

    def a_star(self, start, end):
        self.distances[start[0]][start[1]] = 0
        self.previous[start[0]][start[1]] = start

        heap = [(self.heuristic(start, end), start)]
        while heap:
            self.operations += 1
            current = heapq.heappop(heap)[1]
            if current == end:
                break
            if self.visited[current[0]][current[1]]:
                continue
            self.visited[current[0]][current[1]] = True

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if self.is_valid(neighbor):
                    if direction in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # Diagonal movement, distance is sqrt(2)
                        new_distance = self.distances[current[0]][current[1]] + math.sqrt(2)
                    else:
                        # Horizontal/Vertical movement, distance is 1
                        new_distance = self.distances[current[0]][current[1]] + 1

                    if new_distance < self.distances[neighbor[0]][neighbor[1]]:
                        self.distances[neighbor[0]][neighbor[1]] = new_distance
                        self.previous[neighbor[0]][neighbor[1]] = current
                        heapq.heappush(heap, (self.heuristic(neighbor, end)
                                              + new_distance, neighbor))

        return self.get_path(start, end)

    def heuristic(self, node, end):
        return math.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2)


    def is_valid(self, node):
        return (0 <= node[0] < self.rows
                and 0 <= node[1] < self.cols
                and not self.visited[node[0]][node[1]]
                and self.maze[node[0]][node[1]] == 0)

    def get_path(self, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = self.previous[current[0]][current[1]]
        path.append(start)
        return path[::-1]
