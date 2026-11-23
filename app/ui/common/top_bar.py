"""Top bar widget."""

from __future__ import annotations

from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class TopBar(QWidget):
    """Application top bar."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.addWidget(QLabel("ATC Operation Manager"))
        layout.addStretch()
