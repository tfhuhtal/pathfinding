import unittest
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar

class TestAStar(unittest.TestCase):
    """
    Test the A-star class
    """
    def setUp(self):
        self.maze = [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.a_star = AStar(self.maze)
        self.dijkstra = Dijkstra(self.maze)

    def test_a_star(self):
        start = (0, 0)
        end = (3, 3)
        expected_path = [(0, 0), (0, 1), (1, 2), (2, 3), (3, 3)]
        self.assertEqual(self.a_star.a_star(start, end), expected_path)

    def test_a_star_len(self):
        start = (3, 0)
        end = (0, 0)
        self.assertEqual(len(self.a_star.a_star(start, end)), len(self.dijkstra.dijkstra(start, end)))

    def test_a_star_same_start_end(self):
        start = (0, 0)
        end = (0, 0)
        expected_path = [(0, 0)]
        self.assertEqual(self.a_star.a_star(start, end), expected_path)

    def test_a_star_invalid_start_end(self):
        start = (-1, -1)
        end = (4, 4)
        with self.assertRaises(IndexError):
            self.a_star.a_star(start, end)

    def test_a_star_wall(self):
        start = (1, 0)
        end = (1, 1)
        with self.assertRaises(TypeError):
            self.a_star.a_star(start, end)

    def test_a_star_large_maze(self):
        large_maze = [[0] * 50 for _ in range(50)]
        dijkstra = Dijkstra(large_maze)
        a_star = AStar(large_maze)
        start = (0, 0)
        end = (49, 49)
        self.assertEqual(a_star.a_star(start, end), dijkstra.dijkstra(start, end))

    def test_a_star_path(self):
        maze = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ]

        dijkstra = Dijkstra(maze)
        a_star = AStar(maze)
        start = (0, 0)
        end = (9, 9)
        self.assertEqual(dijkstra.dijkstra(start, end), a_star.a_star(start, end))

    def test_a_star_path_rev(self):
        maze = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ]

        dijkstra = Dijkstra(maze)
        a_star = AStar(maze)
        start = (9, 9)
        end = (0, 0)
        self.assertEqual(dijkstra.dijkstra(start, end), a_star.a_star(start, end))

    def test_operation_count(self):
        start = (0, 0)
        end = (3, 3)
        self.a_star.a_star(start, end)
        self.assertEqual(self.a_star.operations, 5)
