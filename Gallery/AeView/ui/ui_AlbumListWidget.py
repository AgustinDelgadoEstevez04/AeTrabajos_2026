# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlbumListWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

import AeView.resources.resource_rc

class Ui_AlbumListWidget(object):
    def setupUi(self, AlbumListWidget):
        if not AlbumListWidget.objectName():
            AlbumListWidget.setObjectName(u"AlbumListWidget")
        AlbumListWidget.resize(209, 294)
        self.verticalLayout_2 = QVBoxLayout(AlbumListWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(AlbumListWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createAlbumButton = QPushButton(self.frame)
        self.createAlbumButton.setObjectName(u"createAlbumButton")
        icon = QIcon()
        icon.addFile(u":/icons/album-add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createAlbumButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.createAlbumButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.albumList = QListView(AlbumListWidget)
        self.albumList.setObjectName(u"albumList")

        self.verticalLayout_2.addWidget(self.albumList)


        self.retranslateUi(AlbumListWidget)

        QMetaObject.connectSlotsByName(AlbumListWidget)
    # setupUi

    def retranslateUi(self, AlbumListWidget):
        AlbumListWidget.setWindowTitle(QCoreApplication.translate("AlbumListWidget", u"Form", None))
        self.createAlbumButton.setText(QCoreApplication.translate("AlbumListWidget", u" Create", None))
    # retranslateUi

