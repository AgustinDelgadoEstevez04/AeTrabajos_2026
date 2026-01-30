import sys
sys.path.append('/AeView/resources')

from PySide6.QtWidgets import QApplication
from AeView.Widgets.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
