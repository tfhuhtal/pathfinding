import unittest
from algorithms.dijkstra import Dijkstra


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
        expected_path = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        res = self.dijkstra.search(start, end)
        self.assertEqual((res[0], res[1]), (expected_path, 10))

    def test_dijkstra_no_path(self):
        start = (0, 0)
        end = (1, 0)
        with self.assertRaises(TypeError):
            self.dijkstra.search(start, end)

    def test_dijkstra_same_start_end(self):
        start = (0, 0)
        end = (0, 0)
        expected_path = [(0, 0)]
        res = self.dijkstra.search(start, end)
        self.assertEqual(res[0], expected_path)

    def test_dijkstra_invalid_start_end(self):
        start = (-1, -1)
        end = (4, 4)
        with self.assertRaises(IndexError):
            self.dijkstra.search(start, end)

    def test_dijkstra_wall(self):
        start = (1, 0)
        end = (1, 1)
        with self.assertRaises(TypeError):
            self.dijkstra.search(start, end)

    def test_dijkstra_large_maze(self):
        large_maze = [[0] * 50 for _ in range(50)]
        dijkstra = Dijkstra(large_maze)
        start = (0, 0)
        end = (49, 49)
        expected_path = [(0, 0)] + [(i, i) for i in range(1, 50)]
        res = dijkstra.search(start, end)
        self.assertEqual((res[0], res[1]), (expected_path, 2564))

    def test_dijkstra_large_maze_all_directions(self):
        maze = [
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        ]
        dijkstra = Dijkstra(maze)

        start = (1, 3)
        end = (9, 9)
        expected_path = [
            (1, 3), (2, 3), (3, 3), (4, 3),
            (5, 3), (6, 2), (7, 2), (8, 3),
            (9, 4), (8, 5), (7, 5), (6, 5),
            (5, 5), (4, 5), (3, 5), (2, 6),
            (1, 6), (0, 7), (1, 8), (2, 8),
            (3, 8), (4, 8), (5, 8), (6, 8),
            (7, 8), (8, 8), (9, 9)
        ]
        res = dijkstra.search(start, end)
        self.assertEqual((res[0], res[1]), (expected_path, 80))

    def test_operation_count(self):
        start = (0, 0)
        end = (3, 3)
        res = self.dijkstra.search(start, end)
        self.assertEqual(res[1], 10)
