from ..inputs import read_lines
from ..polymer import react


if __name__ == "__main__":
    polymer: str = list(read_lines("day5"))[0]
    result = react(polymer)
    print(f"{len(result)} units after reaction")
