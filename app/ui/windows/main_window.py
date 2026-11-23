"""Main window for ATC Operation Manager."""

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from app.ui.common.page_container import PageContainer
from app.ui.common.sidebar import Sidebar
from app.ui.common.status_bar import StatusBar
from app.ui.common.top_bar import TopBar


class MainWindow(QMainWindow):
    """Primary application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ATC Operation Manager")
        self.resize(1280, 800)

        central_widget = QWidget(self)
        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        root_layout.addWidget(TopBar(self))

        body = QWidget(self)
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        body_layout.addWidget(Sidebar(self))
        body_layout.addWidget(PageContainer(self), 1)
        root_layout.addWidget(body, 1)

        self.setCentralWidget(central_widget)
        self.setStatusBar(StatusBar(self))
