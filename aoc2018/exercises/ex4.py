from ..inputs import read_lines
from ..guards import DutyLog


if __name__ == "__main__":
    log = DutyLog(read_lines("day4"))
    guard = log.sleepiest_guard
    print("Part one", guard * log.sleepiest_minute(guard))
