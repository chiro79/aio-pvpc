"""ESIOS API handler for HomeAssistant. Utils."""

from datetime import datetime, timezone


def ensure_utc_time(ts: datetime) -> datetime:
    """Return tz-aware datetime in UTC from any datetime."""
    if ts.tzinfo is None:
        return datetime(*ts.timetuple()[:6], tzinfo=timezone.utc)
    elif str(ts.tzinfo) != str(timezone.utc):
        return ts.astimezone(timezone.utc)
    return ts
