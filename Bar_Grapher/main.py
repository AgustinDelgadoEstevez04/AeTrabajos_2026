import sys
from PySide6.QtWidgets import QApplication
from mainform import MainForm

def main():
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec())

main()
