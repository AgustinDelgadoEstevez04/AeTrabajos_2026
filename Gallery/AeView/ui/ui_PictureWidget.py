# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PictureWidget.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import AeView.resources.resource_rc

class Ui_PictureWidget(object):
    def setupUi(self, PictureWidget):
        if not PictureWidget.objectName():
            PictureWidget.setObjectName(u"PictureWidget")
        PictureWidget.resize(589, 366)
        self.verticalLayout_2 = QVBoxLayout(PictureWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(PictureWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.backButton = QPushButton(self.frame)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMaximumSize(QSize(130, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/back-to-gallery.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.backButton)

        self.nameLabel = QLabel(self.frame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMaximumSize(QSize(130, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/photo-delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.previousButton = QPushButton(self.frame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMaximumSize(QSize(50, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/photo-previous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previousButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.frame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMaximumSize(QSize(50, 16777215))
        self.nextButton.setMouseTracking(False)
        self.nextButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/photo-next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextButton.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.nextButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.pictureLabel = QLabel(PictureWidget)
        self.pictureLabel.setObjectName(u"pictureLabel")
        self.pictureLabel.setScaledContents(False)
        self.pictureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.pictureLabel)


        self.retranslateUi(PictureWidget)

        QMetaObject.connectSlotsByName(PictureWidget)
    # setupUi

    def retranslateUi(self, PictureWidget):
        PictureWidget.setWindowTitle(QCoreApplication.translate("PictureWidget", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("PictureWidget", u" Back", None))
        self.nameLabel.setText(QCoreApplication.translate("PictureWidget", u"Foto.jpg", None))
        self.deleteButton.setText(QCoreApplication.translate("PictureWidget", u" Delete", None))
        self.previousButton.setText("")
        self.nextButton.setText("")
        self.pictureLabel.setText("")
    # retranslateUi

