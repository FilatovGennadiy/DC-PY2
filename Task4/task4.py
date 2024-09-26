class Rent:
    """ Базовый класс, описывающий арендадательские компании """

    def __init__(self, name: str):
        self.name = name  # название арендадательской компании
        self.num_element = 0  # число элементов

    def add_element(self, num_new_element: int) -> int:  # добавление элементов, который покупатель может арендовать
        """
        Метод увеличивает число элементов
        :param num_new_element: количество элементов
        :return:
        """
        self.num_element += num_new_element

    def extract_element(self, num: int) -> str:  # вызов заданого элемента бронирования
        ...
        """
        Метод вызывает заданное нужный элемент
        :param num номер элемента 
        :return: 
        """

    def change_element(self, element_1: int, element_2: int) -> None:  # element_1 и element_2 - номера элементов
        ...
        """ 
        Метод может менять арендаторов элементов
        :param element_1, element_2 номер элемента 
        :return: 
        """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self):
        return f'Компания по аренде "{self.name}"'


class Hotel:
    """Дочерний класс арендодтельских компаний - отели """

    def __init__(self, name: str, num_of_rooms: int, num_of_beds: int, num_of_stars: str):
        super().__init__(name)  # расширение производного класса(наследование)
        self.num_of_rooms = num_of_rooms  # Количество комнат в номере
        self.num_of_beds = num_of_beds  # Количество кроватей
        self.num_of_stars = num_of_stars  # Количество звёзд у отеля

    def add_element(self, num_element: int) -> int:
        super().add_element(num_element)  # наследование метода

    def extract_element(self, num_of_rooms: int, num_of_beds: int) -> int:
        super().extract_element(num_of_rooms, num_of_beds)  # наследование метода

    def __repr__(self) -> str:  # перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.num_of_rooms!r}, {self.num_of_beds!r}, ' \
               f'{self.num_of_stars!r}) '

    def __str__(self):
        return f'Отель "{self.name}"'  # перегрузка метода str


class CarRental:
    """Дочерний класс, компания по аренде машин"""

    def __init__(self, name: str, car: str, colour: str):
        super().__init__(name)  # наследование
        self.car = car  # тригонометрическая формула, по умолчанию синус
        self.colour = colour

    def add_element(self, num_element: int) -> int:
        super().add_element(num_element)  # наследование метода

    def extract_element(self, car: str) -> int:
        super().extract_element(car)  # наследование метода и перегрузка, так как выделяется определённая машина

    def __repr__(self) -> str:  # перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.car!r},{self.colour!r})'

    def __str__(self):
        return f'Аренда автомобилей "{self.name}"'  # перегрузка метода str, так как таблица имеет другое название
