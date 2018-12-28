from collections import Counter
from dataclasses import dataclass
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

    def license_value(self) -> int:
        lic = self.navlicense
        root = LicenseNode(lic[0], lic[1], [], [])
        node = root
        i = 2
        stack: List[LicenseNode] = [root]

        while stack:
            node = stack[-1]

            if node.complete:
                # no children or metadata to add
                stack.pop()  # go back to parent
                continue

            if node.children_complete:
                # no more children to add, but maybe metadata
                mdlast = i + node.mlen
                md = lic[i:mdlast]
                i = mdlast
                node.metadata.extend(md)
                continue

            # we still have children to add
            child = LicenseNode(lic[i], lic[i + 1], [], [])
            i = i + 2
            node.children.append(child)
            stack.append(child)

        return root.value


@dataclass
class LicenseNode:
    clen: int
    mlen: int
    children: List["LicenseNode"]
    metadata: List[int]

    @property
    def children_complete(self) -> bool:
        return self.clen == len(self.children)

    @property
    def metadata_complete(self) -> bool:
        return self.mlen == len(self.metadata)

    @property
    def complete(self) -> bool:
        return self.children_complete and self.metadata_complete

    @property
    def value(self) -> int:
        if not self.complete:
            raise Exception(f"incomplete: {self}")
        if self.children:
            nodes = [
                self.children[i - 1] for i in self.metadata if i > 0 and i <= self.clen
            ]
            return sum(map(lambda n: n.value, nodes))
        return sum(self.metadata)

    def __repr__(self) -> str:
        return f"({self.clen}:{self.children} {self.mlen}:{self.metadata})"
