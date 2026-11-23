"""Runtime application state helpers."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AppState:
    """Simple runtime state container."""

    current_user: str | None = None
    active_page: str = "dashboard"
    flags: dict[str, str] = field(default_factory=dict)
