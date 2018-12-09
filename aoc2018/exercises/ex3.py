from ..inputs import read_lines
from ..fabric import ClaimChecker


if __name__ == "__main__":
    checker = ClaimChecker(read_lines("day3"))
    print("Multiply-claimed square count:", checker.claimed_by_multiple())
    print("Claims without overlaps:", checker.nonoverlapping())
