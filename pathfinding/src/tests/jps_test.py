import unittest
from PIL import Image
from algorithms.jps import JPS
from algorithms.astar import AStar


class TestJPS(unittest.TestCase):
    """
    Test the Jump Point Search class
    """

    def setUp(self):
        self.maze = [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.jps = JPS(self.maze)
        self.astar = AStar(self.maze)

    def test_jps(self):
        start = (0, 0)
        end = (3, 3)
        expected_path = [(0, 0), (0, 1), (1, 2), (2, 3), (3, 3)]
        result = self.jps.search(start, end)
        self.assertEqual(result[0], expected_path)

    def test_jps_no_path(self):
        start = (0, 0)
        end = (1, 3)
        expected_path = None
        result = self.jps.search(start, end)
        self.assertEqual(result[0], expected_path)

    def test_jps_invalid_start_and_end(self):
        start = (-1, -1)
        end = (4, 4)
        expected_path = None
        result = self.jps.search(start, end)
        self.assertEqual(result[0], expected_path)

    def test_jps_same_start_and_end(self):
        start = (0, 0)
        end = (0, 0)
        expected_path = [(0, 0)]
        result = self.jps.search(start, end)
        self.assertEqual(result[0], expected_path)

    def test_jps_path(self):
        maze = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ]

        jps = JPS(maze)
        start = (0, 0)
        end = (9, 9)
        expected_path = [(0, 0), (0, 5), (1, 6), (2, 5),
                         (2, 1), (3, 0), (7, 0), (8, 1),
                         (8, 6), (8, 8), (9, 9)]
        result = jps.search(start, end)
        self.assertEqual(result[0], expected_path)

    def test_jps_massive(self):
        image = Image.open("maps/map1.png")
        pixels = image.load()
        width, height = image.size
        matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for i in range(height)]
                   for j in range(width)])

        start = (170, 383)
        end = (589, 253)

        jps = JPS(matrix)
        astar = AStar(matrix)

        path = jps.search(start, end)
        res = astar.search(start, end)
        self.assertEqual(round(path[2], 8), round(res[2], 8))
