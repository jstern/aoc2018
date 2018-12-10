from collections import Counter
import logging
import os
import re
from typing import Iterable

logging.basicConfig(level=getattr(logging, os.environ.get("LOG_LEVEL", "INFO")))
log = logging.getLogger(__name__)


class LogProcessor:
    start_re = re.compile(r"Guard #(\d+) begins shift")

    def __init__(self, entries: Iterable[str]):
        self.guard: str = ""
        self.asleep_at: int = -1
        self.incidents: Counter = Counter()
        self.process_entries(entries)

    def process_entries(self, entries: Iterable[str]) -> None:
        for entry in entries:
            tstamp, event = entry[12:].split("] ")
            minute: int = int(tstamp[3:])
            self.handle_shift_start(minute, event)
            self.handle_doze(minute, event)
            self.handle_wake(minute, event)

    def handle_shift_start(self, minute: int, event: str) -> None:
        start_match = self.start_re.match(event)
        if start_match:
            self.log_incident(60)
            self.guard = start_match.group(1)
            self.asleep_at = -1
            log.debug(f"{self.guard} started shift")

    def handle_doze(self, minute: int, event: str) -> None:
        if event == "falls asleep":
            log.debug(f"{self.guard} fell asleep at {minute}")
            self.asleep_at = minute

    def handle_wake(self, minute: int, event: str) -> None:
        if event == "wakes up":
            log.debug(f"{self.guard} woke up at {minute}")
            self.log_incident(minute)
            self.asleep_at = -1

    def log_incident(self, awake_at: int) -> None:
        if self.guard != "" and self.asleep_at != -1:
            log.debug(f"{self.guard} was asleep from {self.asleep_at} to {awake_at}")
            for minute in range(self.asleep_at, awake_at):
                self.incidents.update({(self.guard, minute): 1})


class DutyLog:
    def __init__(self, entries: Iterable[str]):
        self.entries = sorted(entries)
        self.incidents = LogProcessor(self.entries).incidents
