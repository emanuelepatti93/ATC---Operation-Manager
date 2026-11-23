"""Top bar widget."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class TopBar(QWidget):
    """Application top bar."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("TopBar")
        self.setFixedHeight(56)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 0, 18, 0)
        layout.setSpacing(12)

        title = QLabel("ATC Operation Manager")
        title.setObjectName("TopBarTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        subtitle = QLabel("Shift planning • presence • reports")
        subtitle.setObjectName("TopBarSubtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch(1)
