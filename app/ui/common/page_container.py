"""Central page container for stacked views."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QStackedWidget, QVBoxLayout, QWidget


class PageContainer(QStackedWidget):
    """Container that hosts the main application pages."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        dashboard = QWidget(self)
        layout = QVBoxLayout(dashboard)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("Dashboard")
        title.setStyleSheet("font-size: 28px; font-weight: 700;")
        subtitle = QLabel(
            "Versione dimostrativa dell'interfaccia del gestionale ATC. "
            "Qui verranno aggiunte statistiche, calendario, turni e report."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color: #94a3b8; font-size: 14px;")

        card = QLabel("Anteprima area contenuti\n\n- Presenze\n- Turni\n- Posizioni\n- Report")
        card.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        card.setStyleSheet(
            """
            QLabel {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid #243244;
                border-radius: 16px;
                padding: 18px;
                font-size: 15px;
                line-height: 1.5;
            }
            """
        )
        card.setMinimumHeight(240)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(card)
        layout.addStretch(1)

        self.addWidget(dashboard)
