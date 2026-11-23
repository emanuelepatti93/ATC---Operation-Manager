"""Sidebar navigation widget."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget


class Sidebar(QListWidget):
    """Left navigation sidebar."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSpacing(4)
        self.addItems([
            "Dashboard",
            "Presenze",
            "Turni",
            "Posizioni",
            "Report",
            "Impostazioni",
        ])
