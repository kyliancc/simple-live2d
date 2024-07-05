# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'texturebox.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TextureBox(object):
    def setupUi(self, TextureBox):
        if not TextureBox.objectName():
            TextureBox.setObjectName(u"TextureBox")
        TextureBox.resize(333, 62)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TextureBox.sizePolicy().hasHeightForWidth())
        TextureBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(TextureBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.container = QWidget(TextureBox)
        self.container.setObjectName(u"container")
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, -1)
        self.icon = QLabel(self.container)
        self.icon.setObjectName(u"icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy1)
        self.icon.setMinimumSize(QSize(30, 30))
        self.icon.setMaximumSize(QSize(30, 30))
        self.icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon)

        self.name = QLabel(self.container)
        self.name.setObjectName(u"name")

        self.horizontalLayout.addWidget(self.name)

        self.nameEdit = QLineEdit(self.container)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setEnabled(True)
        self.nameEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.nameEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(TextureBox)

        QMetaObject.connectSlotsByName(TextureBox)
    # setupUi

    def retranslateUi(self, TextureBox):
        TextureBox.setWindowTitle(QCoreApplication.translate("TextureBox", u"Form", None))
        self.icon.setText(QCoreApplication.translate("TextureBox", u"icon", None))
        self.name.setText(QCoreApplication.translate("TextureBox", u"name", None))
    # retranslateUi

