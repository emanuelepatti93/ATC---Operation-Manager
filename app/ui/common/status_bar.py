"""Status bar widget helpers."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QStatusBar


class StatusBar(QStatusBar):
    """Application status bar."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.addPermanentWidget(QLabel("Pronto"))
