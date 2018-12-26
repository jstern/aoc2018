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

    """
    def test_license_number(self):
        lic = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        dev = device.Device(navlicense=lic)
        self.assertEqual(dev.license_number(), 138)
    """


class LicenseTests(unittest.TestCase):
    def test_no_children(self):
        with self.subTest("no md"):
            lic = [0, 0]
            self.assertEqual(device.Device(navlicense=lic).license_number(), 0)
        with self.subTest("1 md"):
            lic = [0, 1, 2]
            self.assertEqual(device.Device(navlicense=lic).license_number(), 2)
        with self.subTest(">1 md"):
            lic = [0, 2, 3, 4]
            self.assertEqual(device.Device(navlicense=lic).license_number(), 7)

    def test_with_children(self):
        lic = [2, 2, 0, 1, 3, 0, 1, 4, 5, 6]
        self.assertEqual(device.Device(navlicense=lic).license_number(), 18)

    def test_example(self):
        lic = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        self.assertEqual(device.Device(navlicense=lic).license_number(), 138)
