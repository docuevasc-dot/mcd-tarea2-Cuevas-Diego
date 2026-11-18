from __future__ import annotations

from enum import Enum


class Event(str, Enum):
    """Observable event names used across MiniChat."""

    MESSAGES_UPDATED = "messages_updated"
    GENERATING_START = "generating_start"
    GENERATING_DONE = "generating_done"
    GENERATING_ERROR = "generating_error"
    CONFIG_CHANGED = "config_changed"
    EXPORT_DONE = "export_done"