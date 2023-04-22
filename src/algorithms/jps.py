import math
import heapq

class JumpPointSearch:
    """
    Jump Point Search Algorithm
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

    def search(self, start, end):
        # Initialize start node
        self.distances[start[0]][start[1]] = 0
        self.visited[start[0]][start[1]] = True
        heap = [(0, start)]
        heapq.heapify(heap)

        # Main loop
        while heap:
            _, current = heapq.heappop(heap)
            self.operations += 1

            # Goal found
            if current == end:
                return self.get_path(start, end)

            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                jump_point = self.jump(neighbor, current, end)
                if jump_point is None:
                    continue

                # Calculate tentative distance to jump point
                tentative_distance = self.distances[current[0]][current[1]] + \
                    math.sqrt((jump_point[0] - current[0]) ** 2 + (jump_point[1] - current[1]) ** 2)

                # Update distance and previous node if better path found
                if tentative_distance < self.distances[jump_point[0]][jump_point[1]]:
                    self.distances[jump_point[0]][jump_point[1]] = tentative_distance
                    self.previous[jump_point[0]][jump_point[1]] = current

                    # Add to heap for further exploration
                    priority = tentative_distance + self.heuristic(jump_point, end)
                    heapq.heappush(heap, (priority, jump_point))

                    # Mark as visited
                    self.visited[jump_point[0]][jump_point[1]] = True

        # Goal not found
        return None

    def jump(self, node, parent, end):
        """
        Jumps from the given node to its furthest ancestor that can be reached in a straight line.
        Returns None if no jump point is found in this direction.
        """
        dx, dy = node[0] - parent[0], node[1] - parent[1]

        # If the node is outside the grid or blocked, return None
        if not self.is_valid(node) or self.maze[node[0]][node[1]]:
            return None

        # If the node is the end point, return it
        if node == end:
            return node

        # Diagonal movement
        if dx != 0 and dy != 0:
            # Check for forced neighbors
            if (self.is_valid((node[0] - dx, node[1])) and self.maze[node[0] - dx][node[1]]) or \
               (self.is_valid((node[0], node[1] - dy)) and self.maze[node[0]][node[1] - dy]):
                return node

            # Recurse on diagonal
            jump_node = self.jump((node[0] + dx, node[1]), node, end)
            if jump_node:
                return jump_node
            jump_node = self.jump((node[0], node[1] + dy), node, end)
            if jump_node:
                return jump_node

        # Horizontal movement
        elif dx != 0:
            # Check for forced neighbors
            if (self.is_valid((node[0], node[1] + 1)) and self.maze[node[0]][node[1] + 1]) or \
               (self.is_valid((node[0], node[1] - 1)) and self.maze[node[0]][node[1] - 1]):
                return node

            # Recurse on horizontal
            jump_node = self.jump((node[0] + dx, node[1]), node, end)
            if jump_node:
                return jump_node

        # Vertical movement
        else:
            # Check for forced neighbors
            if (self.is_valid((node[0] + 1, node[1])) and self.maze[node[0] + 1][node[1]]) or \
               (self.is_valid((node[0] - 1, node[1])) and self.maze[node[0] - 1][node[1]]):
                return node

            # Recurse on vertical
            jump_node = self.jump((node[0], node[1] + dy), node, end)
            if jump_node:
                return jump_node

        # No jump point found in this direction
        return None

    def get_neighbors(self, node):
        neighbors = []
        for direction in self.directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if self.is_valid(neighbor) and not self.maze[neighbor[0]][neighbor[1]]:
                neighbors.append(neighbor)
        return neighbors

    def is_valid(self, pos):
        row, col = pos
        return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0])

    def heuristic(self, node, end):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])
    
    def get_path(self, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = self.previous[current[0]][current[1]]
        path.append(start)
        return path[::-1]
