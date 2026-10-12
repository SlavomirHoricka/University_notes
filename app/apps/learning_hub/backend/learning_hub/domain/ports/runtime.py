from datetime import datetime
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime:
        """Return an aware UTC instant."""
        ...


class IdGenerator(Protocol):
    def new(self, prefix: str) -> str:
        """Allocate an operational ID once, before persistence."""
        ...
