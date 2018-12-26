from collections import Counter
from itertools import chain, cycle
from typing import Iterable, List, Set


class Device:
    """A fancy wrist device."""

    def __init__(self, navlicense: List[int] = []):
        self.freq: int = 0
        self.navlicense: List[int] = navlicense

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

    def matching_letters(self, box_ids: Iterable[str]) -> str:
        def matchables(idstr: str) -> Iterable[str]:
            for i in range(len(idstr)):
                j = i + 1
                yield idstr[:i] + "_" + idstr[j:]

        counts = Counter(chain.from_iterable(matchables(idstr) for idstr in box_ids))
        return counts.most_common(1)[0][0].replace("_", "")

    def license_number(self) -> int:
        tot: int = 0
        stack = [[1, 0]]  # pretend there's a root header: 1 child, 0 md
        for n in self.navlicense:
            if len(stack[-1]) == 1:
                # we have a child count, add an md count
                stack[-1].append(n)
            elif len(stack[-1]) == 2 and stack[-1][0] > 0:
                # read more children, decrement number left to read
                stack[-1][0] = stack[-1][0] - 1
                stack.append([n])
            elif stack[-1][1] > 0:
                # read more metadata, decrement number left to read
                stack[-1][1] = stack[-1][1] - 1
                tot = tot + n

            if stack[-1] == [0, 0]:
                # nothing left to read for current node
                stack.pop()

        return tot

    def license_number_r(self) -> int:
        # come back and see if this is less brain-wracking done recursively
        raise NotImplementedError()
