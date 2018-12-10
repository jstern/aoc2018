from typing import List, Tuple


def reacts(u1: str, u2: str) -> bool:
    return abs(ord(u1) - ord(u2)) == 32


def start(polymer: str, exclude: Tuple[str, str]) -> Tuple[List[str], int]:
    result = []
    for i, unit in enumerate(polymer):
        if unit in exclude:
            continue
        else:
            result.append(unit)
            break
    return result, i


def step(result: List[str], unit: str, exclude: Tuple[str, str]):
    if unit in exclude:
        return
    try:
        rx = reacts(unit, result[-1])
    except IndexError:
        rx = False
    if rx:
        result.pop()
    else:
        result.append(unit)


def react(polymer: str, without: str = "") -> str:
    exclude = (without.upper(), without.lower())
    result, i = start(polymer, exclude)
    i = i + 1
    for unit in polymer[i:]:
        step(result, unit, exclude)
    return "".join(result)
