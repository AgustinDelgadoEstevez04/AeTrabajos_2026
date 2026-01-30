from PySide6.QtCore import Qt,QModelIndex,QRect,QSize
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QStyle

BANNER_HEIGHT = 20
BANNER_COLOR = 0x303030
BANNER_ALPHA = 200
BANNER_TEXT_COLOR = 0xffffff
HIGHLIGHT_ALPHA = 100

class PictureDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        painter.save()

        pixmap = index.model().data(index, Qt.DecorationRole)
        if pixmap:
            painter.drawPixmap(option.rect.x(), option.rect.y(), pixmap)

            banner_rect = QRect(option.rect.x(), option.rect.y(), pixmap.width(), BANNER_HEIGHT)
            banner_color = QColor(BANNER_COLOR)
            banner_color.setAlpha(BANNER_ALPHA)
            painter.fillRect(banner_rect, banner_color)

            filename = index.model().data(index, Qt.DisplayRole)
            painter.setPen(QColor(BANNER_TEXT_COLOR))
            painter.drawText(banner_rect, Qt.AlignCenter, filename)

            if option.state & QStyle.State_Selected:
                selected_color = option.palette.highlight().color()
                selected_color.setAlpha(HIGHLIGHT_ALPHA)
                painter.fillRect(option.rect, selected_color)

        painter.restore()

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        pixmap = index.model().data(index, Qt.DecorationRole)
        if pixmap:
            return pixmap.size()
        return QSize()

