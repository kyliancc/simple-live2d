from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget

from view.textures.texturebox_ui import Ui_TextureBox


class TextureBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TextureBox()
        self.ui.setupUi(self)

        self.ui.nameEdit.setVisible(False)

    def init(self, icon: QImage, name: str = 'My texture'):
        self.ui.icon.setPixmap(QPixmap.fromImage(icon))
        self.ui.name.setText(name)
