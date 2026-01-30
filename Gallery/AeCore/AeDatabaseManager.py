from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from AeCore.AeAlbumDao import AeAlbumDao
from AeCore.AePictureDao import AePictureDao

DATABASE_FILENAME = "gallery.db"  # Nombre del archivo de la base de datos


class AeDatabaseManager:
    _instance = None  # Variable de clase para guardar la única instancia

    def __new__(cls):
        # Si aún no existe una instancia, se crea
        if cls._instance is None:
            # Crea la instancia real
            cls._instance = super().__new__(cls)

            # Marca que aun no esta inicializada
            cls._instance._initialized = False

        # Devuelve la instancia
        return cls._instance

    def __init__(self, path: str = DATABASE_FILENAME):
        if self._initialized:
            return

        self._database = QSqlDatabase.addDatabase("QSQLITE")
        self._database.setDatabaseName(path)

        if not self._database.open():
            print("Database connection: Error")
        else:
            print("Database connection: OK")

        print("DB REAL PATH:", self._database.databaseName())
        import os
        print("DB EXISTS:", os.path.exists(self._database.databaseName()))

        # PRAGMA debe ejecutarse con un QSqlQuery vacío asociado a la DB
        query = QSqlQuery(self._database)
        query.exec("PRAGMA foreign_keys = ON")

        # la conexión está lista
        self.album_dao = AeAlbumDao(self)
        self.picture_dao = AePictureDao(self)

        # Inicializar las tablas en la base de datos
        self.album_dao.init()
        self.picture_dao.init()

        self._initialized = True

    @staticmethod
    def instance():
        return AeDatabaseManager()

    def close(self):
        if self._database.isOpen():
            self._database.close()