import unittest

from aoc2018.polymer import react, reacts


examples = [
    ("aA", ""),
    ("abBA", ""),
    ("abAB", "abAB"),
    ("aabAAB", "aabAAB"),
    ("dabAcCaCBAcCcaDA", "dabCBAcaDA"),
]


class TestPolymer(unittest.TestCase):
    def test_reacts(self):
        with self.subTest("same unit different polarity react"):
            self.assertTrue(reacts("a", "A"))
            self.assertTrue(reacts("B", "b"))

        with self.subTest("same unit same polarity doesn't react"):
            self.assertFalse(reacts("C", "C"))

        with self.subTest("different units don't react"):
            self.assertFalse(reacts("d", "E"))

    def test_react(self):
        for i, example in enumerate(examples):
            with self.subTest(f"example {i}"):
                self.assertEqual(react(example[0]), example[1])
