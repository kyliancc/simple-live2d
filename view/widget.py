import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication

from view.widget_ui import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def init(self, name: str, widget: QWidget):
        self.ui.name.setText(name)
        self.ui.verticalLayout_3.addWidget(widget)


def test():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    test()
