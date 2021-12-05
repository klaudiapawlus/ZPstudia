
class Ocena:
    def __init__(self , userId: int, movieId: int, rating: float, timestamp: int):
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
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
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
         self._rating = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
         self._timestamp = value
