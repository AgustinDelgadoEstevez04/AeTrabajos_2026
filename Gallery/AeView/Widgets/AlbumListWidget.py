from PySide6.QtWidgets import QWidget, QVBoxLayout, QInputDialog, QLineEdit
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import os

from AeCore.AeAlbumModel import AeAlbumModel
from AeCore.AeAlbum import AeAlbum
from AeView.ui.ui_AlbumListWidget import Ui_AlbumListWidget


class AlbumListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._album_model: AeAlbumModel = None
        self.ui = Ui_AlbumListWidget()
        self.ui.setupUi(self)
        self._setup()


    def _setup(self):
        # Establecer icono desde código
        base = os.path.dirname(__file__)
        resources_path = os.path.join(base, "resources", "icons")

        add_icon_path = os.path.join(resources_path, "album-add.png")
        if os.path.exists(add_icon_path):
            self.ui.createAlbumButton.setIcon(QIcon(add_icon_path))
        else:
            self.ui.createAlbumButton.setIcon(QIcon.fromTheme("folder-new"))

        self.ui.createAlbumButton.clicked.connect(self._create_album)

    def set_model(self, model: AeAlbumModel):
        self._album_model = model
        self.ui.albumList.setModel(self._album_model)

    def set_selection_model(self, selection_model: QItemSelectionModel):
        self.ui.albumList.setSelectionModel(selection_model)

    def _create_album(self):
        if not self._album_model:
            return

        album_name, ok = QInputDialog.getText(
            self,
            "Create a new Album",
            "Choose a name",
            QLineEdit.Normal,
            "New album"
        )

        if ok and album_name:
            album = AeAlbum(album_name)
            created_index = self._album_model.add_album(album)
            self.ui.albumList.setCurrentIndex(created_index)