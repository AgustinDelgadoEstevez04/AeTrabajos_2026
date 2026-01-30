from typing import List
from PySide6.QtCore import Qt, QModelIndex,QAbstractListModel,Slot

from AeCore.AePicture import AePicture
from AeCore.AeDatabaseManager import AeDatabaseManager
from AeCore.AeAlbumModel import AeAlbumModel

class AePictureModel(QAbstractListModel):

    class Roles:
        UrlRole = Qt.UserRole + 1
        FilePathRole = Qt.UserRole + 2

    def __init__(self, album_model:AeAlbumModel, parent = None):
        super().__init__(parent)
        self._db = AeDatabaseManager.instance()
        self._album_id: int = -1
        self._pictures: List[AePicture] = []

        album_model.rowsRemoved.connect(self.delete_pictures_for_album)

    def add_picture(self, picture:AePicture)->QModelIndex:
        rows = self.rowCount()
        self.beginInsertRows(QModelIndex(), rows, rows)
        new_picture = AePicture(picture.file_url().toLocalFile())
        self._db.picture_dao.add_picture_in_album(self._album_id, new_picture)
        self._pictures.append(new_picture)
        self.endInsertRows()
        return self.index(rows, 0)

    def rowCount(self, parent: QModelIndex = QModelIndex())->int:
        return len(self._pictures)

    def data(self, index:QModelIndex, role:int = Qt.DisplayRole):
        if not self._is_index_valid(index):
            return None

        picture = self._pictures[index.row()]

        if role == Qt.DisplayRole:
            return picture.file_url().fileName()
        elif role == self.Roles.UrlRole:
            return picture.file_url()
        elif role == self.Roles.FilePathRole:
            return  picture.file_url().toLocalFile()

        return None

    def removeRows(self, row: int, count:int, parent:QModelIndex = QModelIndex())->bool:
        if row <0 or row >= self.rowCount() or count < 0 or (row + count)>self.rowCount():
            return False

        self.beginRemoveRows(parent,row,row+count-1)
        count_left=count
        while count_left>0:
            count_left-=1
            picture = self._pictures[row + count_left]
            self._db.picture_dao.remove_picture(picture.id())

        del self._pictures[row:row+count]
        self.endRemoveRows()
        return True

    def roleNames(self):
        roles = {
            Qt.DisplayRole: b"name",
            self.Roles.FilePathRole: b"filepath",
            self.Roles.UrlRole: b"url"
        }
        return roles

    def set_album_id(self, album_id:int):
        self.beginResetModel()
        self._album_id = album_id
        self._load_pictures(self._album_id)
        self.endResetModel()

    def clear_album(self):
        self.set_album_id(-1)

    @Slot()

    def delete_pictures_for_album(self):
        self._db.picture_dao.remove_pictures_for_album(self._album_id)
        self.clear_album()

    def _load_pictures(self,album_id:int):
        if album_id<=0:
            self._pictures=[]
            return
        self._pictures = self._db.picture_dao.pictures_for_album(album_id)

    def _is_index_valid(self, index:QModelIndex)->bool:
        if index.row()<0 or index.row()>=self.rowCount() or not index.isValid():
            return False
        return True







