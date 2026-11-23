"""Entry point for ATC Operation Manager."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.ui.windows.main_window import MainWindow


def main() -> int:
    """Start the desktop application."""
    app = QApplication(sys.argv)
    app.setApplicationName("ATC Operation Manager")

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
