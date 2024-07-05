import sys

from PySide6.QtWidgets import QApplication

from view.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
