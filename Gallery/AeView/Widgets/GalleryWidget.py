from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QModelIndex, QItemSelectionModel

from AeCore.AeAlbumModel import AeAlbumModel

from AeView.Widgets.ThumbnailProxyModel import ThumbnailProxyModel
from AeView.ui.ui_GalleryWidget import Ui_GalleryWidget


class GalleryWidget(QWidget):
    picture_activated = Signal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GalleryWidget()
        self.ui.setupUi(self)
        self._setup()



    def _setup(self):
        self.ui.albumListWidget.setMaximumWidth(250)
        self.ui.albumWidget.picture_activated.connect(self.picture_activated)

    def set_album_model(self, album_model: AeAlbumModel):
        self.ui.albumListWidget.set_model(album_model)
        self.ui.albumWidget.set_album_model(album_model)

    def set_album_selection_model(self, album_selection_model: QItemSelectionModel):
        self.ui.albumListWidget.set_selection_model(album_selection_model)
        self.ui.albumWidget.set_album_selection_model(album_selection_model)

    def set_picture_model(self, picture_model: ThumbnailProxyModel):
        self.ui.albumWidget.set_picture_model(picture_model)

    def set_picture_selection_model(self, picture_selection_model: QItemSelectionModel):
        self.ui.albumWidget.set_picture_selection_model(picture_selection_model)
