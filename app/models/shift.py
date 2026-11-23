"""Shift domain model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Shift:
    """Represents a work shift."""

    code: str
    start_time: str
    end_time: str
