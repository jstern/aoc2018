import os
import re
from typing import Dict, Iterable, List


step_re = re.compile(r"^Step (.) must be finished before step (.) can begin.$")


def read_steps(inp: Iterable[str]):
    res: Dict[str, List[str]] = {}
    for constraint in inp:
        match = step_re.match(constraint)
        if match is None:
            # satisfy type checker
            continue
        step, req = match.group(2), match.group(1)
        res.setdefault(step, []).append(req)
        res.setdefault(req, [])
    return {step: res[step] for step in sorted(res.keys())}


def get_next(steps):
    res = None
    for step, reqs in steps.items():
        if len(reqs) == 0:
            res = step
            break
    if res:
        del steps[res]
    return res


def on_finish(step, steps):
    for reqs in steps.values():
        if step in reqs:
            reqs.remove(step)


def init(workers: int, inp: Iterable[str]):
    return {
        "time": -1,
        "steps": read_steps(inp),
        "workers": [{"step": None, "start": None} for i in range(workers)],
        "done": "",
    }


def tick(state):
    now = state["time"] + 1
    state["time"] = now

    # pass 1: see who's finished
    for worker in state["workers"]:
        step = worker["step"]
        if step and done(step, worker["start"], now):
            state["done"] = f"{state['done']}{worker['step']}"
            on_finish(step, state["steps"])
            worker["step"] = None

    # pass 2: distribute new work
    for worker in state["workers"]:
        if worker["step"] is None:
            worker["step"] = get_next(state["steps"])
            worker["start"] = now

    show(state)


def duration(step: str) -> int:
    return ord(step) - 64 + int(os.environ.get("TICK_MIN", 60))


def done(step: str, start: int, now: int) -> bool:
    return duration(step) <= (now - start)


def all_done(state):
    return len(state["steps"]) == 0 and not any(w["step"] for w in state["workers"])


def show(state):
    now = state["time"]
    wrks = "\t".join(w["step"] or "." for w in state["workers"])
    print(f"{now}\t{wrks}\t{state['done']}")


def run(workers: int, inp: Iterable[str]):
    state = init(workers, inp)
    while not all_done(state):
        tick(state)
