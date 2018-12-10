from multiprocessing import Pool
from string import ascii_uppercase
from typing import Tuple

from ..inputs import read_lines
from ..polymer import react


if __name__ == "__main__":
    polymer: str = list(read_lines("day5"))[0]
    result = react(polymer)
    print(f"{len(result)} units after reaction")

    def polymer_len(without: str) -> Tuple[str, int]:
        return without, len(react(polymer, without=without))

    pool = Pool()
    results = sorted(pool.map(polymer_len, ascii_uppercase), key=lambda x: x[1])
    print("Shortest possible:", results[0])
