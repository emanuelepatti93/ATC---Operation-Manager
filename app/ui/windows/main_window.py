"""Main window for ATC Operation Manager."""

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    """Primary application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ATC Operation Manager")
        self.resize(1280, 800)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel("ATC Operation Manager"))
        self.setCentralWidget(central_widget)
