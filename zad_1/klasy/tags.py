
class Tag:
    def __init__(self , userId: int, movieId: int, tag: str, timestamp: int):
        self._userId = userId
        self._movieId = movieId
        self._tag = tag
        self._timestamp = timestamp

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def movieId(self):
        return self._movieId

    @movieId.setter
    def movieId(self, value):
        self._movieId = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
         self._tag = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
         self._timestamp = value
