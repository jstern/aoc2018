from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True, order=True)
class Point2D:
    x: int
    y: int

    @classmethod
    def from_str(cls, desc: str) -> "Point2D":
        return cls(*map(int, desc.split(",")))

    def __repr__(self):
        return f"({self.x}, {self.y})"


@dataclass(frozen=True)
class Rect:
    o: Point2D
    w: int
    h: int

    def points(self) -> Iterable[Point2D]:
        x = self.o.x
        while x <= self.o.x + self.w:
            y = self.o.y
            while y <= self.o.y + self.h:
                yield Point2D(x, y)
                y = y + 1
            x = x + 1


def points(inp: Iterable[str]) -> List[Point2D]:
    return sorted([Point2D.from_str(desc) for desc in inp])


def md(a: Point2D, b: Point2D) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def cross(o: Point2D, a: Point2D, b: Point2D) -> int:
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def hull_points(points: List[Point2D]) -> List[Point2D]:
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain

    lh: List[Point2D] = []  # lower hull
    uh: List[Point2D] = []  # upper hull

    for point in points:
        while len(lh) >= 2 and cross(lh[-2], lh[-1], point) <= 0:
            lh.pop()
        lh.append(point)

    for point in reversed(points):
        while len(uh) >= 2 and cross(uh[-2], uh[-1], point) <= 0:
            uh.pop()
        uh.append(point)

    return lh[:-1] + uh[:-1]


def box(hull: List[Point2D]) -> Rect:
    (lx, hx, ly, hy) = (hull[0].x, hull[0].x, hull[0].y, hull[0].y)
    for p in hull[1:]:
        if p.x < lx:
            lx = p.x
        if p.x > hx:
            hx = p.x
        if p.y < ly:
            ly = p.y
        if p.y > hy:
            hy = p.y
    return Rect(Point2D(lx, ly), hx - lx, hy - ly)


def max_area(points: List[Point2D]) -> int:
    hull = hull_points(points)
    rect = box(hull)
    interior = [p for p in points if p not in hull]
    distances: Dict = {}

    # find the distances to each candidate point from each point in the rectangle
    # (is the rectangle a mistake? could there be points outside the rectangle closest to interior points?)
    for point in rect.points():
        for point2 in points:
            distances.setdefault(point, {})[point2] = md(point, point2)

    # for each point in the rectangle, which interior points are closest?
    int_areas: Dict[Point2D, int] = {}
    for point in interior:
        a: int = 0
        for dists in distances.values():
            sdists: List[Tuple[Point2D, int]] = sorted(dists.items(), key=lambda i: i[1])
            mindist = sdists[0][1]
            if sdists[1][1] == mindist:
                # > 1 candidate is same distance
                continue
            if sdists[0][0] == point:
                # there's one unique closest point, and it's this one
                # so include it in the area
                a = a + 1
        int_areas[point] = a

    return sorted(int_areas.values())[-1]
