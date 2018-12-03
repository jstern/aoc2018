import unittest

from aoc2018 import device


class DeviceTests(unittest.TestCase):
    def test_starts_with_frequency_0(self):
        self.assertEqual(device.Device().freq, 0)

    def test_processes_changes_to_frequency(self):
        changes = ["-1", "5", "-1"]
        dev = device.Device()
        dev.process_changes(changes)
        self.assertEqual(dev.freq, 3)

    def test_calibrate_finds_first_repeated_frequency(self):
        cases = ((["+1", "-1"], 0), (["+3", "+3", "+4", "-2", "-4"], 10))
        for changes, result in cases:
            dev = device.Device()
            dev.calibrate(changes)
            self.assertEqual(dev.freq, result)

    def test_warehouse_checksum(self):
        ids = ("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab")
        self.assertEqual(device.Device().warehouse_checksum(ids), 12)

    def test_similar_boxes(self):
        ids = ("abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz")
        self.assertEqual(device.Device().matching_letters(ids), "fgij")
