from ..inputs import read_lines
from ..device import Device


def part1() -> int:
    device = Device()
    device.process_changes(read_lines("ex1"))
    return device.freq


def part2() -> int:
    device = Device()
    device.calibrate(read_lines("ex1"))
    return device.freq


if __name__ == "__main__":
    print(part1())
    print(part2())
