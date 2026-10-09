#!/usr/bin/env python3
"""Calculate a simple SM-2-style next review date for one objective."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo


def next_review(outcome: str, previous_interval: int | None, reviewed_on: date) -> dict:
    if outcome in {"initial", "failure"}:
        interval = 1
    elif outcome == "success":
        if previous_interval is None or previous_interval < 1:
            raise ValueError("success needs a positive previous interval")
        interval = 6 if previous_interval == 1 else max(
            previous_interval + 1, int(previous_interval * 2.5 + 0.5)
        )
    else:
        raise ValueError("outcome must be initial, success, or failure")
    return {"interval_days": interval, "due_date": (reviewed_on + timedelta(days=interval)).isoformat()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("outcome", choices=["initial", "success", "failure"])
    parser.add_argument("--previous-interval", type=int)
    parser.add_argument("--review-date", type=date.fromisoformat)
    args = parser.parse_args()
    today = datetime.now(ZoneInfo("Europe/Prague")).date()
    print(json.dumps(next_review(args.outcome, args.previous_interval, args.review_date or today)))


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sample = date(2026, 10, 3)
        assert next_review("initial", None, sample)["due_date"] == "2026-10-04"
        assert next_review("success", 1, sample)["interval_days"] == 6
        assert next_review("success", 6, sample)["interval_days"] == 15
        assert next_review("failure", 60, sample)["interval_days"] == 1
        print("ok")
    else:
        main()
