import re
from datetime import UTC, datetime
from uuid import uuid4


class SystemClock:
    def now(self) -> datetime:
        return datetime.now(UTC)


class UUIDGenerator:
    def new(self, prefix: str) -> str:
        if not re.fullmatch(r"[a-z]{3}", prefix):
            raise ValueError("Operational ID prefix must contain three lowercase letters")
        return f"{prefix}_{uuid4()}"
