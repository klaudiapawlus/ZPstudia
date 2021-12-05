class Film:
    def __init__(self ,movieId: int, title: str, generes: str):
        self._movieId = movieId
        self._title = title
        self._generes = generes

    @property
    def generes(self):
        return self._generes

    @generes.setter
    def generes(self, value):
        self._generes = value

    @property
    def movieId(self):
        return self._movieId

    @movieId.setter
    def movieId(self, value):
        self._movieId = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
         self._titled = value

