from ..inputs import read_lines
from ..grid import max_area, points


if __name__ == "__main__":
    print(max_area(points(read_lines("day6"))))
