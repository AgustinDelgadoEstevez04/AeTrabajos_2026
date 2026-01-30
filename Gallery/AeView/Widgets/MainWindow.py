from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import QModelIndex, QItemSelectionModel

from AeCore.AeAlbumModel import AeAlbumModel
from AeCore.AePictureModel import AePictureModel
from AeView.Widgets.GalleryWidget import GalleryWidget
from AeView.Widgets.PictureWidget import PictureWidget
from AeView.Widgets.ThumbnailProxyModel import ThumbnailProxyModel
from AeView.ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup()


    def _setup(self):
        self._gallery_widget = GalleryWidget(self)
        self._picture_widget = PictureWidget(self)
        self.stacked_widget = QStackedWidget(self)

        album_model = AeAlbumModel(self)
        album_selection_model = QItemSelectionModel(album_model, self)
        self._gallery_widget.set_album_model(album_model)
        self._gallery_widget.set_album_selection_model(album_selection_model)

        picture_model = AePictureModel(album_model, self)
        thumbnail_model = ThumbnailProxyModel(self)
        thumbnail_model.setSourceModel(picture_model)

        picture_selection_model = QItemSelectionModel(thumbnail_model,self)
        self._gallery_widget.set_picture_model(thumbnail_model)
        self._gallery_widget.set_picture_selection_model(picture_selection_model)
        self._picture_widget.set_model((thumbnail_model))
        self._picture_widget.set_selection_model(picture_selection_model)


        self._gallery_widget.picture_activated.connect(self._display_picture)
        self._picture_widget.back_to_gallery.connect(self._display_gallery)

        self.stacked_widget.addWidget(self._gallery_widget)
        self.stacked_widget.addWidget(self._picture_widget)
        self._display_gallery()

        self.setCentralWidget(self.stacked_widget)

    def _display_gallery(self):
        self.stacked_widget.setCurrentWidget(self._gallery_widget)

    def _display_picture(self,index: QModelIndex):
        self.stacked_widget.setCurrentWidget(self._picture_widget)











