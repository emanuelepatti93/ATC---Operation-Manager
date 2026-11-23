"""Central page container for stacked views."""

from __future__ import annotations

from PySide6.QtWidgets import QStackedWidget


class PageContainer(QStackedWidget):
    """Container that hosts the main application pages."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
