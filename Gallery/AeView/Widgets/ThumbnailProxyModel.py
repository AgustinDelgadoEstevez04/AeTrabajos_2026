from PySide6.QtCore import Qt,QModelIndex,QIdentityProxyModel,QAbstractItemModel
from PySide6.QtGui import QPixmap
from AeCore.AePictureModel import AePictureModel

THUMBNAIL_SIZE = 350


class ThumbnailProxyModel(QIdentityProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._thumbnails = {}

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if role != Qt.DecorationRole:
            return super().data(index, role)

        filepath = self.sourceModel().data(index, AePictureModel.Roles.FilePathRole)
        return self._thumbnails.get(filepath)

    def setSourceModel(self, source_model: QAbstractItemModel):
        super().setSourceModel(source_model)
        if not source_model:
            return

        source_model.modelReset.connect(self._reload_thumbnails)
        source_model.rowsInserted.connect(self._on_rows_inserted)

    def picture_model(self) -> AePictureModel:
        return self.sourceModel()

    def _on_rows_inserted(self, parent: QModelIndex, first: int, last: int):
        self._generate_thumbnails(self.index(first, 0), last - first + 1)

    def _reload_thumbnails(self):
        self._thumbnails.clear()
        self._generate_thumbnails(self.index(0, 0), self.rowCount())

    def _generate_thumbnails(self, start_index: QModelIndex, count: int):
        if not start_index.isValid():
            return

        model = start_index.model()
        last_index = start_index.row() + count

        for row in range(start_index.row(), last_index):
            filepath = model.data(model.index(row, 0), AePictureModel.Roles.FilePathRole)
            pixmap = QPixmap(filepath)
            thumbnail = pixmap.scaled(
                THUMBNAIL_SIZE, THUMBNAIL_SIZE,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self._thumbnails[filepath] = thumbnail

