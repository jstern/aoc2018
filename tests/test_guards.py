import unittest
import random

from aoc2018.guards import DutyLog


example = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
]


class TestGuards(unittest.TestCase):
    def test_sorts_entries(self):
        raw = example[:]
        random.shuffle(raw)
        log = DutyLog(raw)
        self.assertNotEqual(raw, example)
        self.assertEqual(log.entries, example)

    def test_tallies_sleep_incidents(self):
        log = DutyLog(example)

        with self.subTest("finds sleepiest guard"):
            self.assertEqual(log.sleepiest_guard, 10)

        with self.subTest("finds sleepiest minute for guard"):
            self.assertEqual(log.sleepiest_minute(10), 24)

        with self.subTest("finds sleepiest guard/minute combo"):
            self.assertEqual(log.sleepiest_guard_minute, (99, 45))
