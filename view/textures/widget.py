from PySide6.QtCore import QDir
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QWidget, QFileDialog

from view.textures.texturebox import TextureBox
from view.textures.widget_ui import Ui_TextureWidget


class TextureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TextureWidget()
        self.ui.setupUi(self)

        self.ui.addTexture.clicked.connect(self.add_texture)

    def add_texture(self):
        paths, _ = QFileDialog.getOpenFileNames(self, 'Select Texture File', QDir.homePath(), 'All files (*.*)')
        if not paths:
            return

        print(paths)
        images = [QImage(path) for path in paths]
        print(images)

        for image in images:
            texture_box = TextureBox(self)
            texture_box.init(image)
            self.ui.verticalLayout_2.insertWidget(0, texture_box)
