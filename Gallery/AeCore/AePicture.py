from PySide6.QtCore import QUrl

class AePicture:
    def __init__(self, file_path: str = ""):
        self._id: int = -1
        self._album_id: int = -1

        if file_path:
            self._file_url: QUrl = QUrl.fromLocalFile(file_path)
        else:
            self._file_url: QUrl = QUrl()

    @classmethod
    def from_url(cls, file_url: QUrl):
        picture = cls()
        picture._file_url = file_url
        return picture

    def id(self) -> int:
        return self._id

    def set_id(self, id: int):
        self._id = id

    def album_id(self) -> int:
        return self._album_id

    def set_album_id(self, album_id: int):
        self._album_id = album_id

    def file_url(self) -> QUrl:
        return self._file_url

    def set_file_url(self, file_url):
        if isinstance(file_url, str):
            self._file_url = QUrl(file_url)
        else:
            self._file_url = file_url
