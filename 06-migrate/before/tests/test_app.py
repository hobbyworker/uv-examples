from datetime import datetime, timezone

from app import age


def test_age():
    now = datetime(2026, 10, 10, tzinfo=timezone.utc)
    assert age("2025-08-05T12:00:00Z", now) == "1y 2m 4d"
