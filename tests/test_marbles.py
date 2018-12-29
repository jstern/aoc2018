import unittest

from aoc2018.marbles import MarbleGame


class TestMarbles(unittest.TestCase):
    def test_first_turn(self):
        game = MarbleGame(players=1, hi=1)
        game.play()
        self.assertEqual(game.circle, [0, 1])
        self.assertEqual(game.current_marble, 1)

    def test_second_turn(self):
        game = MarbleGame(players=2, hi=2)
        game.play()
        self.assertEqual(game.circle, [0, 2, 1])
        self.assertEqual(game.current_marble, 2)

    def test_22nd_turn(self):
        game = MarbleGame(players=9, hi=22)
        game.play()
        expected = [
            0,
            16,
            8,
            17,
            4,
            18,
            9,
            19,
            2,
            20,
            10,
            21,
            5,
            22,
            11,
            1,
            12,
            6,
            13,
            3,
            14,
            7,
            15,
        ]
        self.assertEqual(game.circle, expected)
        self.assertEqual(game.current_marble, 22)

    def test_23rd_turn(self):
        game = MarbleGame(players=9, hi=23)
        game.play()
        expected = [
            0,
            16,
            8,
            17,
            4,
            18,
            19,
            2,
            20,
            10,
            21,
            5,
            22,
            11,
            1,
            12,
            6,
            13,
            3,
            14,
            7,
            15,
        ]
        self.assertEqual(game.circle, expected)
        self.assertEqual(game.current_marble, 19)
        self.assertEqual(game.scores[4], 32)
        self.assertEqual(game.winner, (5, 32))
