from typing import List
from PySide6.QtSql import QSqlDatabase,QSqlQuery

from AeCore.AeAlbum import AeAlbum

from AeCore.utils.sql_debug import debug_query


class AeAlbumDao:
    def __init__(self, database_manager):
        self._database = database_manager._database

    def init(self):
        # Comprueba si la tabla "albums" no existe aún
        if "albums" not in self._database.tables():

            # Crea un objeto para ejecutar SQL
            query = QSqlQuery(self._database)

            # Crea la tabla con id autoincremental y un campo de texto 'name'
            query.exec("CREATE TABLE albums (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

            # Muestra si la consulta fue correcta o tuvo errores
            debug_query(query)

    def add_album(self, album: AeAlbum):
        print("AlbumDao REAL:", __file__)
        print("DEBUG Album recibido:", album.id(), album.name())

        query = QSqlQuery(self._database)
        query.prepare("INSERT INTO albums (name) VALUES (?)")
        query.addBindValue(album.name())

        if not query.exec():
            debug_query(query)
            return

        album.set_id(query.lastInsertId())
        debug_query(query)

    def update_album(self, album:AeAlbum):

        query = QSqlQuery(self._database)
        query.prepare("UPDATE albums SET name = (:name) WHERE id = (:id)")
        query.bindValue(":name", album.name())
        query.bindValue(":id", album.id())
        query.exec()
        debug_query(query)

    def remove_album(self, id:int):
        query = QSqlQuery(self._database)
        query.prepare("DELETE FROM albums WHERE id = (:id)")
        query.bindValue(":id", id)
        query.exec()
        debug_query(query)

    def albums(self)-> List[AeAlbum]:
        query = QSqlQuery("SELECT * FROM albums", self._database)
        query.exec()
        album_list=[]
        while query.next():
            album=AeAlbum()
            album.set_id(query.value("id"))
            album.set_name(query.value("name"))
            album_list.append(album)
        return album_list








