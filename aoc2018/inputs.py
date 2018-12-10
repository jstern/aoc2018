import os
from typing import Iterable


def input_path(name: str) -> str:
    return os.path.join("inputs", f"{name}.txt")


def read_lines(name: str) -> Iterable[str]:
    with open(input_path(name), "rb") as inp:
        for line in inp:
            yield line.decode("utf-8").strip()
