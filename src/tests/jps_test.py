import unittest
from algorithms.jps import JumpPointSearch
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
        self.jps = JumpPointSearch(self.maze)

    def test_jps(self):
        start = (0, 0)
        end = (3, 3)
        expected_path = [(0, 0), (0, 2), (2, 2), (3, 3)]
        self.assertEqual(self.jps.jump_point_search(start, end), expected_path)

    def test_jps_invalid_start_end(self):
        start = (-1, -1)
        end = (4, 4)
        with self.assertRaises(IndexError):
            self.jps.jump_point_search(start, end)

    def test_jps_wall(self):
        start = (1, 0)
        end = (1, 1)
        with self.assertRaises(TypeError):
            self.jps.jump_point_search(start, end)

    def test_jps_large_maze(self):
        large_maze = [[0] * 50 for _ in range(50)]
        jps = JumpPointSearch(large_maze)
        a_star = AStar(large_maze)
        start = (0, 0)
        end = (49, 49)
        self.assertEqual(jps.jump_point_search(start, end), a_star.a_star(start, end))
