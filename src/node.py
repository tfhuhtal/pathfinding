class Node:
    """
    A node class for pathfinding algorithms
    """
    def __init__(self, col, row, parent=None, g=0, h=0):
        self.col = col
        self.row = row
        self.parent = parent
        self.g = g
        self.h = h

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def __repr__(self):
        return f"({self.col}, {self.row})"
