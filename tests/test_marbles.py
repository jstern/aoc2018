import unittest

from aoc2018.marbles import MarbleGame


class TestMarbles(unittest.TestCase):
    def test_examples(self):
        for players, hi, score in [
            (9, 25, 32),
            (10, 1618, 8317),
            (13, 7999, 146373),
            (17, 1104, 2764),
            (21, 6111, 54718),
            (30, 5807, 37305),
            (452, 71250, 388844),
        ]:
            with self.subTest((players, hi)):
                game = MarbleGame(players=players, hi=hi)
                game.play()
                self.assertEqual(game.winner[1], score)
