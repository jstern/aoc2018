from ..inputs import read_lines
from .. import sleigh


if __name__ == "__main__":
    sleigh.run(1, read_lines("day7"))
    print()
    sleigh.run(5, read_lines("day7"))
