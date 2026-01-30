class AeAlbum:
    def __init__(self, name: str = "", id: int = -1):
        self._id = id
        self._name = name

    def id(self) -> int:
        return self._id

    def set_id(self, id: int):
        self._id = id

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name
