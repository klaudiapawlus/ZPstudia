
class Link:
    def __init__(self ,movieId: int, imdbId: str, tmdbId: str):
        self._movieId = movieId
        self._imdbId = imdbId
        self._tmdbId = tmdbId

    @property
    def tmdbId(self):
        return self._tmdbId

    @tmdbId.setter
    def tmdbId(self, value):
        self._tmdbId = value

    @property
    def movieId(self):
        return self._movieId

    @movieId.setter
    def movieId(self, value):
        self._movieId = value

    @property
    def imdbId(self):
        return self._imdbId

    @imdbId.setter
    def imdbId(self, value):
         self._imdbId= value

