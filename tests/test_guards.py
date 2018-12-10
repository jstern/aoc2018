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
        incidents = DutyLog(example).incidents
        self.assertEqual(incidents[("10", 4)], 0)
        self.assertEqual(incidents[("10", 5)], 1)
        self.assertEqual(incidents[("10", 24)], 2)
        self.assertEqual(incidents[("10", 25)], 1)
        self.assertEqual(incidents[("99", 45)], 3)
