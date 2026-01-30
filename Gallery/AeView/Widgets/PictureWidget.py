from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt, QItemSelectionModel, QTimer
from PySide6.QtGui import QPixmap, QResizeEvent, QIcon
import os

from AeCore.AePictureModel import AePictureModel
from AeView.Widgets.ThumbnailProxyModel import ThumbnailProxyModel
from AeView.ui.ui_PictureWidget import Ui_PictureWidget


class PictureWidget(QWidget):
    back_to_gallery = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._model: ThumbnailProxyModel = None
        self._selection_model: QItemSelectionModel = None
        self._pixmap: QPixmap = QPixmap()
        self.ui = Ui_PictureWidget()
        self.ui.setupUi(self)
        self._setup()


    def _setup(self):
        self.ui.pictureLabel.setMinimumSize(1, 1)

        # Establecer iconos desde código
        base = os.path.dirname(__file__)
        resources_path = os.path.join(base, "resources", "icons")

        # Cargar iconos si existen, sino usar iconos del sistema
        back_icon_path = os.path.join(resources_path, "back-to-gallery.png")
        if os.path.exists(back_icon_path):
            self.ui.backButton.setIcon(QIcon(back_icon_path))
        else:
            self.ui.backButton.setIcon(QIcon.fromTheme("go-previous"))

        delete_icon_path = os.path.join(resources_path, "photo-delete.png")
        if os.path.exists(delete_icon_path):
            self.ui.deleteButton.setIcon(QIcon(delete_icon_path))
        else:
            self.ui.deleteButton.setIcon(QIcon.fromTheme("edit-delete"))

        previous_icon_path = os.path.join(resources_path, "photo-previous.png")
        if os.path.exists(previous_icon_path):
            self.ui.previousButton.setIcon(QIcon(previous_icon_path))
        else:
            self.ui.previousButton.setIcon(QIcon.fromTheme("go-previous"))

        next_icon_path = os.path.join(resources_path, "photo-next.png")
        if os.path.exists(next_icon_path):
            self.ui.nextButton.setIcon(QIcon(next_icon_path))
        else:
            self.ui.nextButton.setIcon(QIcon.fromTheme("go-next"))

        self.ui.backButton.clicked.connect(self.back_to_gallery)
        self.ui.deleteButton.clicked.connect(self._delete_picture)
        self.ui.previousButton.clicked.connect(self._go_previous)
        self.ui.nextButton.clicked.connect(self._go_next)

    def set_model(self, model: ThumbnailProxyModel):
        self._model = model

    def set_selection_model(self, selection_model: QItemSelectionModel):
        self._selection_model = selection_model
        if not self._selection_model:
            return
        self._selection_model.selectionChanged.connect(self._load_picture)

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self._update_picture_pixmap()

    def showEvent(self, event):
        """Se ejecuta cuando el widget se hace visible"""
        super().showEvent(event)
        # Actualizar la imagen cuando el widget se muestra
        QTimer.singleShot(0, self._update_picture_pixmap)

    def _go_previous(self):
        current_index = self._selection_model.currentIndex()
        previous_index = self._selection_model.model().index(current_index.row() - 1, 0)
        self._selection_model.setCurrentIndex(previous_index, QItemSelectionModel.SelectCurrent)

    def _go_next(self):
        current_index = self._selection_model.currentIndex()
        next_index = self._selection_model.model().index(current_index.row() + 1, 0)
        self._selection_model.setCurrentIndex(next_index, QItemSelectionModel.SelectCurrent)

    def _delete_picture(self):
        row = self._selection_model.currentIndex().row()
        self._model.removeRow(self._selection_model.currentIndex().row())

        previous_index = self._model.index(row - 1, 0)
        if previous_index.isValid():
            self._selection_model.setCurrentIndex(previous_index, QItemSelectionModel.SelectCurrent)
            return

        next_index = self._model.index(row, 0)
        if next_index.isValid():
            self._selection_model.setCurrentIndex(next_index, QItemSelectionModel.SelectCurrent)
            return

        self.back_to_gallery.emit()

    def _load_picture(self, selected, deselected):
        if not selected.indexes():
            self.ui.nameLabel.setText("")
            self.ui.pictureLabel.setPixmap(QPixmap())
            self.ui.deleteButton.setEnabled(False)
            return

        current = selected.indexes()[0]
        filepath = self._model.data(current, AePictureModel.Roles.FilePathRole)
        self._pixmap = QPixmap(filepath)

        self.ui.nameLabel.setText(self._model.data(current, Qt.DisplayRole))

        # Usar QTimer para asegurar que el widget esté dimensionado antes de escalar
        QTimer.singleShot(0, self._update_picture_pixmap)

        self.ui.previousButton.setEnabled(current.row() > 0)
        self.ui.nextButton.setEnabled(current.row() < (self._model.rowCount() - 1))
        self.ui.deleteButton.setEnabled(True)

    def _update_picture_pixmap(self):
        if self._pixmap.isNull():
            return
        scaled_pixmap = self._pixmap.scaled(
            self.ui.pictureLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.ui.pictureLabel.setPixmap(scaled_pixmap)