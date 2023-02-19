if __name__ == "__main__":
    # Write your solution here
    pass


class Table:
    """ Класс, описывающий автопарк """

    def __init__(self, name: str, color: str):
        self.name = name  # название автопарка
        self.color = color  # цвет машины
        self.num_add_car = 0  # число новых машин

    def add_car(self, num_car: int) -> int:  # добавление элементов в таблицу
        """
        Метод увеличивает число добавленных машин
        :param num_car: количество машин(которых хотят добавить)
        :return:
        """
        self.num_add_car += num_car

    def extract_car(self, num: int) -> int:  # вызов заданного числа элементов таблицы
        ...
        """
        Метод вызывает заданное количество элементов таблицы
        :param num число элементов 
        :return: 
        """

    def change_color(self, id_car: int, color: str) -> None:  # перекрасить машину
        ...

        """ 
        Метод меняет цвет машин
        """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self):
        return f'Автопарк "{self.name}"'



class Particles(Table):
    """Дочерниц класс, Таблица элементарных частиц"""

    def __init__(self, name: str, spin: int, type_part: str, charge: str = "+"):
        super().__init__(name, type_part)  # наследование
        self.charge = charge  # заряд частицы
        self.spin = spin  # спин частицы

    def change_type_part(self, spin1: int, spin2: int) -> None:
        super().change_type_part(spin1,
                                 spin2)  # наследование и перегрузка метода, меняются тип частиц с указанными спинами

    def __repr__(self) -> str:  # перегрузка магического метода repr
        return f'{self.__class__.__name__}({self.name!r}, {self.charge!r}, {self.spin!r})'

    def __str__(self):
        return f'Таблица элементарных частиц "{self.name}"'  # перегрузка метода str