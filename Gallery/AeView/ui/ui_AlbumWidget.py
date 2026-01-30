# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlbumWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import AeView.resources.resource_rc

class Ui_AlbumWidget(object):
    def setupUi(self, AlbumWidget):
        if not AlbumWidget.objectName():
            AlbumWidget.setObjectName(u"AlbumWidget")
        AlbumWidget.resize(669, 269)
        self.verticalLayout = QVBoxLayout(AlbumWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.albumInfoFrame = QFrame(AlbumWidget)
        self.albumInfoFrame.setObjectName(u"albumInfoFrame")
        self.albumInfoFrame.setMinimumSize(QSize(0, 40))
        self.albumInfoFrame.setMaximumSize(QSize(16777215, 40))
        self.albumInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.albumInfoFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 4)
        self.albumName = QLabel(self.albumInfoFrame)
        self.albumName.setObjectName(u"albumName")
        self.albumName.setMinimumSize(QSize(0, 0))
        self.albumName.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.albumName.setFont(font)
        self.albumName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.albumName)

        self.addPicturesButton = QPushButton(self.albumInfoFrame)
        self.addPicturesButton.setObjectName(u"addPicturesButton")
        self.addPicturesButton.setMaximumSize(QSize(130, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.addPicturesButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/photo-add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addPicturesButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addPicturesButton)

        self.editButton = QPushButton(self.albumInfoFrame)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMaximumSize(QSize(130, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/album-edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.albumInfoFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMaximumSize(QSize(130, 16777215))
        self.deleteButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons/album-delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addWidget(self.albumInfoFrame)

        self.thumbnailListView = QListView(AlbumWidget)
        self.thumbnailListView.setObjectName(u"thumbnailListView")

        self.verticalLayout.addWidget(self.thumbnailListView)


        self.retranslateUi(AlbumWidget)

        QMetaObject.connectSlotsByName(AlbumWidget)
    # setupUi

    def retranslateUi(self, AlbumWidget):
        AlbumWidget.setWindowTitle(QCoreApplication.translate("AlbumWidget", u"Form", None))
        self.albumName.setText(QCoreApplication.translate("AlbumWidget", u"Nombre", None))
        self.addPicturesButton.setText(QCoreApplication.translate("AlbumWidget", u" Add pictures", None))
        self.editButton.setText(QCoreApplication.translate("AlbumWidget", u" Edit name", None))
        self.deleteButton.setText(QCoreApplication.translate("AlbumWidget", u" Delete", None))
    # retranslateUi

