def reacts(u1: str, u2: str) -> bool:
    return abs(ord(u1) - ord(u2)) == 32


def react(polymer: str) -> str:
    result = [polymer[0]]
    for unit in polymer[1:]:
        try:
            rx = reacts(unit, result[-1])
        except IndexError:
            rx = False

        if rx:
            result.pop()
        else:
            result.append(unit)
    return "".join(result)
