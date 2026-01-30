# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GalleryWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout)

from AeView.Widgets.AlbumListWidget import AlbumListWidget
from AeView.Widgets.AlbumWidget import AlbumWidget

class Ui_GalleryWidget(object):
    def setupUi(self, GalleryWidget):
        if not GalleryWidget.objectName():
            GalleryWidget.setObjectName(u"GalleryWidget")
        GalleryWidget.resize(1057, 676)
        self.horizontalLayout = QHBoxLayout(GalleryWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.albumWidget = AlbumWidget(GalleryWidget)
        self.albumWidget.setObjectName(u"albumWidget")

        self.horizontalLayout.addWidget(self.albumWidget)

        self.albumListWidget = AlbumListWidget(GalleryWidget)
        self.albumListWidget.setObjectName(u"albumListWidget")

        self.horizontalLayout.addWidget(self.albumListWidget)


        self.retranslateUi(GalleryWidget)

        QMetaObject.connectSlotsByName(GalleryWidget)
    # setupUi

    def retranslateUi(self, GalleryWidget):
        GalleryWidget.setWindowTitle(QCoreApplication.translate("GalleryWidget", u"Form", None))
    # retranslateUi

