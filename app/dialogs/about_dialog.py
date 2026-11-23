"""About dialog placeholder."""

from __future__ import annotations

from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout


class AboutDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("About")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("ATC Operation Manager"))
