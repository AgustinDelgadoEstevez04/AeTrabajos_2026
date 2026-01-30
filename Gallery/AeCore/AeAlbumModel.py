from operator import index
from typing import List
from PySide6.QtCore import Qt, QModelIndex,QAbstractListModel


from AeCore.AeAlbum import AeAlbum
from AeCore.AeDatabaseManager import AeDatabaseManager

class AeAlbumModel(QAbstractListModel):

    class Roles:
        IdRole = Qt.UserRole + 1
        NameRole = Qt.UserRole + 2

    def __init__(self, parent = None):
        super().__init__(parent)
        self._db = AeDatabaseManager.instance()
        self._albums: List[AeAlbum] = self._db.album_dao.albums()

    # Añade un nuevo álbum al modelo y devuelve su índice
    def add_album(self, album: AeAlbum) -> QModelIndex:
        row_index = self.rowCount()
        self.beginInsertRows(QModelIndex(), row_index, row_index)

        # Insertar directamente el álbum recibido
        self._db.album_dao.add_album(album)

        # Añadirlo a la lista interna
        self._albums.append(album)

        self.endInsertRows()
        return self.index(row_index, 0)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len (self._albums)

    # Devuelve datos del modelo según el rol solicitado
    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):

        if not self._is_index_valid(index):
            return None

        # Obtenemos el álbum correspondiente a la fila
        album = self._albums[index.row()]

        # Devolver el ID del álbum
        if role == self.Roles.IdRole:
            return album.id()

        # Devolver el nombre del álbum
        elif role == self.Roles.NameRole or role == Qt.DisplayRole:
            return album.name()

        return None

    # Actualiza datos del modelo (solo el nombre del álbum)
    def setData(self, index: QModelIndex, value, role: int = Qt.EditRole) -> bool:

        # Validar índice y permitir solo edición del nombre
        if not self._is_index_valid(index) or role != self.Roles.NameRole:
            return False

        # Obtener el álbum a modificar
        album = self._albums[index.row()]

        # Actualizar el nombre en memoria
        album.set_name(value)

        # Guardar el cambio en la base de datos
        self._db.album_dao.update_album(album)

        # Avisar a Qt que los datos cambiaron
        self.dataChanged.emit(index, index)

        return True

    def removeRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool:

        # Validar que las filas a borrar están dentro del rango
        if row < 0 or row >= self.rowCount() or count < 0 or (row + count) > self.rowCount():
            return False

        # Avisar a Qt que se van a eliminar filas
        self.beginRemoveRows(parent, row, row + count - 1)

        # Contador para borrar desde el final hacia el inicio
        count_left = count

        # Borrar uno a uno desde atrás
        while count_left > 0:
            count_left -= 1

            # Obtener el álbum correspondiente
            album = self._albums[row + count_left]

            # Borrar el álbum de la base de datos
            self._db.album_dao.remove_album(album.id())

        # Borrar los álbumes de la lista interna del modelo
        del self._albums[row:row + count]

        # Avisar a Qt que la eliminación ha terminado
        self.endRemoveRows()

        return True

    def roleNames(self):
        roles = {
            self.Roles.IdRole: b"id",
            self.Roles.NameRole: b"name"
        }
        return roles

    def _is_index_valid(self, index:QModelIndex)->bool:
        return index.isValid() and index.row() < self.rowCount()














