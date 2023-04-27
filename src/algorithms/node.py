class Node():
    """
    A node class for pathfinding algorithms
    """
    def __init__(self, x, y, parent=None, forced_neighbours=None):
        forced_neighbours = forced_neighbours if forced_neighbours else []
        parent = parent if parent else None
        self.x = x
        self.y = y
        self.parent = parent
        self.forced_neighbours = forced_neighbours
        

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
