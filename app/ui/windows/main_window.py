"""Main window for ATC Operation Manager."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget, QVBoxLayout

from app.ui.common.page_container import PageContainer
from app.ui.common.sidebar import Sidebar
from app.ui.common.status_bar import StatusBar
from app.ui.common.top_bar import TopBar


class MainWindow(QMainWindow):
    """Primary application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ATC Operation Manager")
        self.resize(1440, 900)

        central_widget = QWidget(self)
        central_widget.setObjectName("centralWidget")
        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        top_bar = TopBar(self)
        top_bar.setObjectName("topBar")
        root_layout.addWidget(top_bar)

        body = QWidget(self)
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        sidebar = Sidebar(self)
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(280)
        body_layout.addWidget(sidebar)

        page_container = PageContainer(self)
        page_container.setObjectName("pageContainer")
        body_layout.addWidget(page_container, 1)
        root_layout.addWidget(body, 1)

        status_bar = StatusBar(self)
        status_bar.setObjectName("statusBar")
        root_layout.addWidget(status_bar)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("ATC Operation Manager")
        self._apply_demo_style()

    def _apply_demo_style(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow {
                background: #0f172a;
                color: #e5e7eb;
            }
            QWidget#topBar {
                background: #111827;
                border-bottom: 1px solid #243244;
            }
            QWidget#sidebar {
                background: #0b1220;
                border-right: 1px solid #243244;
            }
            QWidget#pageContainer {
                background: #111827;
            }
            QWidget#statusBar {
                background: #111827;
                border-top: 1px solid #243244;
            }
            QListWidget {
                background: transparent;
                color: #e5e7eb;
                border: none;
                padding: 8px;
                outline: none;
            }
            QListWidget::item {
                padding: 14px 12px;
                margin: 4px 0;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.03);
            }
            QListWidget::item:selected {
                background: #1f3b5b;
                color: white;
            }
            QLabel {
                color: #e5e7eb;
            }
            """
        )
