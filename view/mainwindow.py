import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from view.attributes.widget import AttributeWidget
from view.editor.widget import EditorWidget
from view.parameters.widget import ParameterWidget
from view.textures.widget import TextureWidget

from view.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.attributes.init('Attributes', AttributeWidget(self))
        self.ui.textures.init('Textures', TextureWidget(self))
        self.ui.editor.init('Editor', EditorWidget(self))
        self.ui.parameters.init('Parameters', ParameterWidget(self))

        # self.ui.actionNew.connect(self.new_file)
        # self.ui.actionOpen.connect(self.open_file)

    def new_file(self):
        pass

    def open_file(self):
        pass


def test():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    test()
