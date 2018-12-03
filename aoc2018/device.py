from collections import Counter
from itertools import cycle
from typing import Iterable, Set


class Device:
    """A fancy wrist device."""

    def __init__(self):
        self.freq: int = 0

    def process_changes(self, changes: Iterable[str]) -> None:
        self.freq = self.freq + sum(int(c) for c in changes)

    def calibrate(self, changes: Iterable[str]) -> None:
        seen: Set[int] = {self.freq}
        for change in cycle(changes):
            self.freq = self.freq + int(change)
            if self.freq in seen:
                break
            seen.add(self.freq)

    def warehouse_checksum(self, box_ids: Iterable[str]) -> int:
        twos, threes = 0, 0
        for box_id in box_ids:
            counts = Counter(box_id).values()
            twos = twos + (2 in counts)
            threes = threes + (3 in counts)
        return twos * threes
