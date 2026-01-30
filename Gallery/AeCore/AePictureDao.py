from typing import List
from PySide6.QtSql import QSqlQuery
from AeCore.AePicture import AePicture
from AeCore.utils.sql_debug import debug_query

class AePictureDao:
    def __init__(self, database_manager):
        self._database = database_manager._database

    def init(self):
        if "pictures" not in self._database.tables():
            query = QSqlQuery(self._database)
            query.exec(
                "CREATE TABLE pictures ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "album_id INTEGER, "
                "url TEXT, "
                "FOREIGN KEY(album_id) REFERENCES albums(id) ON DELETE CASCADE)"
            )
            debug_query(query)

    def add_picture_in_album(self, album_id: int, picture: AePicture):
        query = QSqlQuery(self._database)
        query.prepare("INSERT INTO pictures (album_id, url) VALUES (?, ?)")
        query.addBindValue(album_id)
        query.addBindValue(picture.file_url().toString())

        if not query.exec():
            debug_query(query)
            return

        picture.set_id(query.lastInsertId())
        picture.set_album_id(album_id)
        debug_query(query)

    def remove_picture(self, id: int):
        query = QSqlQuery(self._database)
        query.prepare("DELETE FROM pictures WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        debug_query(query)

    def remove_pictures_for_album(self, album_id: int):
        query = QSqlQuery(self._database)
        query.prepare("DELETE FROM pictures WHERE album_id = ?")
        query.addBindValue(album_id)
        query.exec()
        debug_query(query)

    def pictures_for_album(self, album_id: int) -> List[AePicture]:
        query = QSqlQuery(self._database)
        query.prepare("SELECT * FROM pictures WHERE album_id = ?")
        query.addBindValue(album_id)
        query.exec()
        debug_query(query)

        picture_list = []
        while query.next():
            picture = AePicture()
            picture.set_id(query.value("id"))
            picture.set_album_id(query.value("album_id"))
            picture.set_file_url(query.value("url"))
            picture_list.append(picture)

        return picture_list
