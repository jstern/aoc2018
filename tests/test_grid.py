import unittest

import random

from aoc2018 import grid


class TestGrid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        inp = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
        random.shuffle(inp)
        cls.points = grid.points(inp)

    def test_points(self):
        expected = [
            grid.Point2D(*p) for p in [(1, 1), (1, 6), (3, 4), (5, 5), (8, 3), (8, 9)]
        ]
        self.assertEqual(self.points, expected)

    def test_hull_points(self):
        expected = [grid.Point2D(*p) for p in [(1, 1), (8, 3), (8, 9), (1, 6)]]
        self.assertEqual(grid.hull_points(self.points), expected)

    def test_md(self):
        with self.subTest("distance from self is 0"):
            self.assertEqual(0, grid.md(self.points[0], self.points[0]))

        with self.subTest("distance is same regardless of direction"):
            self.assertEqual(
                grid.md(self.points[1], self.points[2]),
                grid.md(self.points[2], self.points[1]),
            )

        with self.subTest("distance is calculated correctly"):
            self.assertEqual(3, grid.md(self.points[2], self.points[3]))
