class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author


class PaperBook:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})'

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Значение указанной переменной должно быть типа int")
        if self.pages <= 0:
            raise TypeError("Значение должно быть положительным")
        self._pages = pages


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})'

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def pages(self, duration: float) -> None:

        if not isinstance(duration, float):
            raise TypeError("Значение duration должно быть типа float")
        if self.duration <= 0:
            raise ValueError('Значение duration должно быть положительным')
        self._duration = duration
