from PySide6.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog, QListView
from PySide6.QtCore import Signal, QModelIndex, QDir, QItemSelectionModel, Qt
from PySide6.QtGui import QIcon
import os

from AeCore.AeAlbumModel import AeAlbumModel
from AeCore.AePicture import AePicture
from AeView.Widgets.ThumbnailProxyModel import ThumbnailProxyModel
from AeView.delegates.PictureDelegate import PictureDelegate
from AeView.ui.ui_AlbumWidget import Ui_AlbumWidget


class AlbumWidget(QWidget):
    picture_activated = Signal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._album_model: AeAlbumModel = None
        self._album_selection_model: QItemSelectionModel = None
        self._picture_model: ThumbnailProxyModel = None
        self._picture_selection_model: QItemSelectionModel = None
        self.ui = Ui_AlbumWidget()
        self.ui.setupUi(self)
        self._setup()



    def _setup(self):
        self.ui.thumbnailListView.setSpacing(5)
        self.ui.thumbnailListView.setResizeMode(QListView.Adjust)
        self.ui.thumbnailListView.setFlow(QListView.LeftToRight)
        self.ui.thumbnailListView.setWrapping(True)
        self.ui.thumbnailListView.setItemDelegate(PictureDelegate(self))

        # Establecer iconos desde código
        base = os.path.dirname(__file__)
        resources_path = os.path.join(base, "resources", "icons")

        add_icon_path = os.path.join(resources_path, "photo-add.png")
        if os.path.exists(add_icon_path):
            self.ui.addPicturesButton.setIcon(QIcon(add_icon_path))
        else:
            self.ui.addPicturesButton.setIcon(QIcon.fromTheme("list-add"))

        edit_icon_path = os.path.join(resources_path, "album-edit.png")
        if os.path.exists(edit_icon_path):
            self.ui.editButton.setIcon(QIcon(edit_icon_path))
        else:
            self.ui.editButton.setIcon(QIcon.fromTheme("document-edit"))

        delete_icon_path = os.path.join(resources_path, "album-delete.png")
        if os.path.exists(delete_icon_path):
            self.ui.deleteButton.setIcon(QIcon(delete_icon_path))
        else:
            self.ui.deleteButton.setIcon(QIcon.fromTheme("edit-delete"))

        self.ui.thumbnailListView.doubleClicked.connect(self.picture_activated)
        self.ui.deleteButton.clicked.connect(self._delete_album)
        self.ui.editButton.clicked.connect(self._edit_album)
        self.ui.addPicturesButton.clicked.connect(self._add_pictures)

        self._clear_ui()

    def set_album_model(self, album_model: AeAlbumModel):
        self._album_model = album_model
        self._album_model.dataChanged.connect(self._on_data_changed)

    def _on_data_changed(self, top_left: QModelIndex, bottom_right: QModelIndex):
        if self._album_selection_model and top_left == self._album_selection_model.currentIndex():
            self._load_album(top_left)

    def set_album_selection_model(self, album_selection_model: QItemSelectionModel):
        self._album_selection_model = album_selection_model
        self._album_selection_model.selectionChanged.connect(self._on_selection_changed)

    def _on_selection_changed(self, selected, deselected):
        if selected.isEmpty():
            self._clear_ui()
            return
        self._load_album(selected.indexes()[0])

    def set_picture_model(self, picture_model: ThumbnailProxyModel):
        self._picture_model = picture_model
        self.ui.thumbnailListView.setModel(picture_model)

    def set_picture_selection_model(self, selection_model: QItemSelectionModel):
        self.ui.thumbnailListView.setSelectionModel(selection_model)

    def _delete_album(self):
        if not self._album_selection_model.selectedIndexes():
            return

        row = self._album_selection_model.currentIndex().row()
        self._album_model.removeRow(row)

        previous_index = self._album_model.index(row - 1, 0)
        if previous_index.isValid():
            self._album_selection_model.setCurrentIndex(
                previous_index, QItemSelectionModel.SelectCurrent
            )
            return

        next_index = self._album_model.index(row, 0)
        if next_index.isValid():
            self._album_selection_model.setCurrentIndex(
                next_index, QItemSelectionModel.SelectCurrent
            )

    def _edit_album(self):
        if not self._album_selection_model.selectedIndexes():
            return

        current_album_index = self._album_selection_model.selectedIndexes()[0]
        old_album_name = self._album_model.data(current_album_index, AeAlbumModel.Roles.NameRole)

        new_name, ok = QInputDialog.getText(
            self,
            "Album name",
            "Change Album name",
            QLineEdit.Normal,
            old_album_name
        )

        if ok and new_name:
            self._album_model.setData(current_album_index, new_name, AeAlbumModel.Roles.NameRole)

    def _add_pictures(self):
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Add pictures",
            QDir.homePath(),
            "Picture files (*.jpg *.png)"
        )

        if filenames:
            last_model_index = None
            for filename in filenames:
                picture = AePicture(filename)
                last_model_index = self._picture_model.picture_model().add_picture(picture)

            if last_model_index:
                self.ui.thumbnailListView.setCurrentIndex(last_model_index)

    def _clear_ui(self):
        self.ui.albumName.setText("")
        self.ui.deleteButton.setVisible(False)
        self.ui.editButton.setVisible(False)
        self.ui.addPicturesButton.setVisible(False)

    def _load_album(self, album_index: QModelIndex):
        album_id = self._album_model.data(album_index, AeAlbumModel.Roles.IdRole)
        self._picture_model.picture_model().set_album_id(album_id)
        self.ui.albumName.setText(self._album_model.data(album_index, Qt.DisplayRole))
        self.ui.deleteButton.setVisible(True)
        self.ui.editButton.setVisible(True)
        self.ui.addPicturesButton.setVisible(True)