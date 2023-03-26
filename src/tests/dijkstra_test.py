import unittest
from dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    """
    Test the Dijkstra class
    """
    def setUp(self):
        self.maze = [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.dijkstra = Dijkstra(self.maze)

    def test_dijkstra(self):
        start = (0, 0)
        end = (3, 3)
        expected_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(self.dijkstra.dijkstra(start, end), expected_path)

    def test_get_closest_node(self):
        self.dijkstra.distances = [
            [0, 1, 2, 3],
            [float('inf'), float('inf'), 3, float('inf')],
            [4, 3, 2, 1],
            [5, float('inf'), float('inf'), 2]
        ]
        self.dijkstra.visited = [
            [True, True, True, True],
            [False, False, True, False],
            [True, True, True, False],
            [True, False, False, False]
        ]
        expected_node = (2, 3)
        self.assertEqual(self.dijkstra.get_closest_node(), expected_node)

    def test_dijkstra_no_path(self):
        start = (0, 0)
        end = (1, 0)
        with self.assertRaises(TypeError):
            self.dijkstra.dijkstra(start, end)

    def test_dijkstra_same_start_end(self):
        start = (0, 0)
        end = (0, 0)
        expected_path = [(0, 0)]
        self.assertEqual(self.dijkstra.dijkstra(start, end), expected_path)

    def test_dijkstra_invalid_start_end(self):
        start = (-1, -1)
        end = (4, 4)
        with self.assertRaises(IndexError):
            self.dijkstra.dijkstra(start, end)

    def test_dijkstra_large_maze(self):
        large_maze = [[0] * 50 for _ in range(50)]
        dijkstra = Dijkstra(large_maze)
        start = (0, 0)
        end = (49, 49)
        expected_path = [(0, 0)] + [(0, i) for i in range(1, 50)] + [(i, 49) for i in range(1, 50)]
        self.assertEqual(dijkstra.dijkstra(start, end), expected_path)