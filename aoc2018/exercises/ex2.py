from ..inputs import read_lines
from ..device import Device


def part1() -> int:
    device = Device()
    return device.warehouse_checksum(read_lines("day2"))


def part2() -> str:
    device = Device()
    return device.matching_letters(read_lines("day2"))


if __name__ == "__main__":
    print(part1())
    print(part2())
