import unittest

from aoc2018 import sleigh


class TestDuration(unittest.TestCase):
    def test_duration_for_step(self):
        self.assertEqual(sleigh.duration("A"), 61)
        self.assertEqual(sleigh.duration("Z"), 86)


class TestDone(unittest.TestCase):
    def test_done(self):
        cases = [
            ["A", 0, 60, False],
            ["A", 0, 61, True],
            ["B", 0, 61, False],
            ["B", 0, 62, True],
        ]
        for case in cases:
            args, expected = case[:-1], case[-1]
            with self.subTest(args):
                self.assertEqual(expected, sleigh.done(*args))


class TestAllDone(unittest.TestCase):
    def test_all_done_when_no_steps_left_and_no_workers_busy(self):
        state = {"steps": {}, "workers": [{"step": None}]}
        self.assertTrue(sleigh.all_done(state))

    def test_not_all_done_when_steps_left(self):
        state = {"steps": {"A": []}, "workers": [{"step": None}]}
        self.assertFalse(sleigh.all_done(state))

    def test_not_all_done_when_workers_busy(self):
        state = {"steps": {}, "workers": [{"step": "A"}]}
        self.assertFalse(sleigh.all_done(state))


class TestInit(unittest.TestCase):
    def test_initializes_state(self):
        state = sleigh.init(1, ["Step B must be finished before step A can begin."])
        expected = {
            "time": -1,
            "steps": {"A": ["B"], "B": []},
            "workers": [{"step": None, "start": None}],
            "done": "",
        }
        self.assertEqual(expected, state)
