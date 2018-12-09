from dataclasses import dataclass
from typing import Dict, Iterable, List, Set, Tuple


@dataclass(frozen=True)
class Claim:
    id: str
    start: Tuple[int, int]
    width: int
    height: int

    @classmethod
    def from_str(cls, desc: str) -> "Claim":
        """Parse from #{id} @ {x},{y}: {w}x{h}"""
        parts = desc.split()
        id = parts[0][1:]
        xy = parts[2].split(",")
        wh = parts[3].split("x")
        return cls(id, (int(xy[0]), int(xy[1][:-1])), int(wh[0]), int(wh[1]))

    @property
    def squares(self) -> Iterable[Tuple[int, int]]:
        x0, y0 = self.start
        for y in range(y0, y0 + self.height):
            for x in range(x0, x0 + self.width):
                yield (x, y)


class ClaimChecker:
    def __init__(self, claims: Iterable[str]):
        self.claimed: Dict[Tuple[int, int], List["Claim"]] = {}
        for desc in claims:
            claim = Claim.from_str(desc)
            for square in claim.squares:
                self.claimed.setdefault(square, []).append(claim)

    def claimed_by_multiple(self) -> int:
        return len([k for k, v in self.claimed.items() if len(v) > 1])

    def nonoverlapping(self) -> List[str]:
        # find claims that never appear in a list of claimants for any other square?
        # keep a counter of how many times each claim has appeared with other claims?
        loners: Set[str] = set()
        sharers: Set[str] = set()
        for claimants in self.claimed.values():
            if len(claimants) == 1:
                loners.add(claimants[0].id)
            else:
                sharers = sharers | set([c.id for c in claimants])
        loners = loners - sharers
        return list(loners)
