import doctest


class Flower:
    def __init__(self, name: str, humidity_lvl: float, water_consumption: float):

        """
            Создание и подготовка объекта "Цветок"

            :param name: Имя цветка
            :param humidity_lvl: Уровень увлажнённости почвы
            :param water_consumption: Расход воды цветком в день

            Пример:
            >>> flower = Flower('Harry', 0.8, 0.05)
        """

        if not isinstance(name, str):
            raise TypeError(f"Задан неверный тип данных, должен быть str, а у вас {type(name)}")
        self.name = name

        if not isinstance(humidity_lvl, float):
            raise TypeError(f"Задан неверный тип данных, должен быть float, а у вас {type(humidity_lvl)}")

        if (humidity_lvl < 0.0) or (humidity_lvl > 1.0):
            raise ValueError('Число должно быть записано в долях')

        self.hlv = humidity_lvl

        if not isinstance(water_consumption, float):
            raise TypeError(f"Задан неверный тип данных, должен быть float, а у вас {type(water_consumption)}")

        if (water_consumption < 0.0) or (water_consumption > 1.0):
            raise ValueError('Число должно быть записано в долях')

        self.wcon = water_consumption

        self.dl = None
        self.init_dl(humidity_lvl)

    def watering(self, amount_of_water: float, time_between_waterings: float) -> None:

        """
            Функция, которая позволяет совершать полив цветка

            :return: Состояние цветка после полива

            Пример:
            >>> flower = Flower('Harry', 0.5, 0.05)
            >>> flower.watering(0.3, 9)
            >>> print(flower.dl)
            The flower is bad
            >>> flower.watering(0.3, 9)
            The flower is dead
            >>> flower.watering(0.3, 9)
            Why are you watering a dead flower?!
        """

        if not isinstance(amount_of_water, float):
            raise TypeError(f"Задан неверный тип данных, должен быть float, а у вас {type(amount_of_water)}")

        if (amount_of_water < 0.0) or (amount_of_water > 1.0):
            raise ValueError('Число должно быть записано в долях')

        if self.dl == "The flower is dead":
            print("Why are you watering a dead flower?!")
            return None

        delta_hlv = self.hlv - time_between_waterings * self.wcon

        if delta_hlv > 0:
            self.hlv = delta_hlv
        else:
            self.dl = "The flower is dead"
            print(self.dl)
            return None

        if self.hlv + amount_of_water < 1.0:
            self.hlv = round(self.hlv + amount_of_water, 2)
        else:
            self.hlv = 1.0
        self.init_dl(self.hlv)

    def init_dl(self, humidity_lvl) -> None:

        """
            Функция инициализации состояние цветка

            :param humidity_lvl: Уровень увлажнённости почвы

            :return: Одно из 4-х состояний цветка

            Пример:
            >>> flower = Flower('Harry', 0.8, 0.05)
            >>> flower.init_dl(flower.hlv)
            >>> print(flower.dl)
            The flower is nice
        """

        if (humidity_lvl >= 0.7) and (humidity_lvl < 0.9):
            self.dl = 'The flower is nice'
        elif ((humidity_lvl >= 0.9) and (humidity_lvl < 0.95)) or ((humidity_lvl >= 0.2) and (humidity_lvl < 0.5)):
            self.dl = 'The flower is bad'
        elif (humidity_lvl >= 0.5) and (humidity_lvl < 0.7):
            self.dl = 'The flower is good'
        elif (humidity_lvl >= 0.95) or (humidity_lvl < 0.2):
            self.dl = 'The flower is dead'


class Gallery:
    def __init__(self, arts: list, capacity: int, address: str) -> None:

        """
            Создание и подготовка объекта "Галерея"

                :param arts: Список картин, в который входят словари с названием картин и их ценами
                :param capacity: Объём хранилища
                :param address: Адрес галереи
                :raise ValueError: Если объём хранилища отрицательное, выходит ошибка

                Пример:
                >>> gal1 = Gallery([{'AAA': 5000},{'BBB': 6021},{'CCC': 1333}], 5, 'Исаакиевская площадь, 1')
        """

        if not isinstance(arts, list):
            raise TypeError(f"Задан неверный тип данных, должен быть list(dict), а у вас {type(arts)}")
        self.arts = arts

        if not isinstance(capacity, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(capacity)}")
        if capacity < 0:
            raise ValueError("Число должно быть положительным")

        for i in range(len(arts)):
            if len(list(arts[i].items())) > 1:
                raise ValueError('Словари в списке должны состоять только из одной пары: название и цена')
            if not isinstance(list(arts[i].keys())[0], str):
                raise ValueError('Ключём должно быть название картины')
            if not isinstance(list(arts[i].values())[0], int):
                raise ValueError('Значением должна быть цена картины')

        self.capacity = capacity

        if not isinstance(address, str):
            raise TypeError(f"Задан неверный тип данных, должен быть str, а у вас {type(address)}")
        self.address = address

    def add_art(self, art: dict) -> None:

        """
            Функция добавляющая новые картины в коллекцию

            :param art: Представленная картина с названием и ценой
            :raise ValueError: Если название записано не в строковом формате, а цена не в целочисленном,
            то выходит ошибка

            Пример:
            >>> gal1 = Gallery([{'AAA': 5000},{'BBB': 6021},{'CCC': 1333}], 5, 'Исаакиевская площадь, 1')
            >>> gal1.add_art({'DDD':323232})
            >>> print(gal1.arts)
            [{'AAA': 5000}, {'BBB': 6021}, {'CCC': 1333}, {'DDD': 323232}]
        """

        if not isinstance(art, dict):
            raise TypeError(f"Задан неверный тип данных, должен быть dict, а у вас {type(art)}")
        if not len(art) == 1:
            raise ValueError('Этот метод принимает на вход работы по одной')
        if not isinstance(list(art.keys())[0], str):
            raise ValueError('Ключём должно быть название картины')
        if not isinstance(list(art.values())[0], int):
            raise ValueError('Значением должна быть цена картины')

        if self.capacity > len(self.arts) + 1:
            self.arts.append(art)
        else:
            print('Gallery is full!')

    def cost(self) -> float:

        """
            Функция позволяющая посчитать сумму всех картин галереи

            :return: Сумма всех стоимостей

            Пример:
            >>> gal1 = Gallery([{'AAA': 5000},{'BBB': 6021},{'CCC': 1333}], 5, 'Исаакиевская площадь, 1')
            >>> gal1.cost()
            12354
        """

        summ = 0
        for i in range(len(self.arts)):
            summ += list((self.arts[i]).values())[0]

        return summ


class BankCard:
    def __init__(self, number: int, pin: int, balance: float) -> None:

        """
            Создание и подготовка объекта "Галерея"

            :param number: Номер карты
            :param pin: Пин-код
            :param balance: Баланс карты
            :raise ValueError: Если длина номера карты и пин-кода не соответсвует 16 и 4, то выходит ошибка

            Пример:
            >>> my_card = BankCard(7999555512348193, 6221, 4221.53)
        """

        if not isinstance(number, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(number)}")
        if len(str(number)) != 16:
            raise ValueError("Номер должен содержать 16 символа")
        self.num = number

        if not isinstance(pin, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(pin)}")
        if len(str(pin)) != 4:
            raise ValueError("Пин должен содержать 4 символа")
        self.pin = pin

        if not isinstance(balance, float):
            raise TypeError(f"Задан неверный тип данных, должен быть float, а у вас {type(balance)}")
        self.balance = balance

    def contribute(self, money: float, pin: int) -> None:

        """
            Метод, позволяющий пополнить карту после правильного введения пин-кода, в случае неправильно введения
            метод сообщит об этом

            :param money: Сумма для пополнения баланса
            :param pin: Введённый пин-код
            :raise ValueError: Если сумма на пополнение отрицательная и длина пин-кода не равна 4, то выходит ошибка

            Пример:
            >>> my_card = BankCard(7999555512348193, 6221, 4221.53)
            >>> my_card.contribute(321.3, 6221)
            >>> print(my_card.balance)
            4542.83
        """

        if not isinstance(money, float):
            raise TypeError(f"Задан неверный тип данных, должен быть float, а у вас {type(money)}")
        if money < 0:
            raise ValueError("Число должно быть положительным")
        if not isinstance(pin, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(pin)}")
        if len(str(pin)) != 4:
            raise ValueError("Пин должен содержать 4 символа")

        if pin == self.pin:
            self.balance += money
            self.balance = round(self.balance, 2)
        else:
            print('Pin is wrong!')

    def charge(self, money: float, pin: int) -> None:

        """
            Метод, позволяющий снять деньги с карты после правильного введения пин-кода, в случае неправильно введения
            метод сообщит об этом

            :param money: Сумма для снятия баланса
            :param pin: Введённый пин-код
            :raise ValueError: Если сумма на снятие отрицательная и длина пин-кода не равна 4, то выходит ошибка

            Пример:
            >>> my_card = BankCard(7999555512348193, 6221, 4221.53)
            >>> my_card.charge(552.5, 6221)
            >>> print(my_card.balance)
            3669.03
        """

        if not isinstance(money, float):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(money)}")
        if money < 0:
            raise ValueError("Число должно быть положительным")
        if not isinstance(pin, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(pin)}")
        if len(str(pin)) != 4:
            raise ValueError("Пин должен содержать 4 символа")

        if pin == self.pin:
            self.balance -= money
            self.balance = round(self.balance, 2)
        else:
            print('Pin is wrong!')

    def change_pin(self, new_pin: int) -> None:

        """
            Метод позволяющий менять пин-код на карте

            :param new_pin: Новый пин-код
            :raise ValueError: Если длина пин-кода не равна 4, то выходит ошибка

            Пример:
            >>> my_card = BankCard(7999555512348193, 6221, 4221.53)
            >>> my_card.change_pin(6421)
            Pin has been changed!
        """

        if not isinstance(new_pin, int):
            raise TypeError(f"Задан неверный тип данных, должен быть int, а у вас {type(new_pin)}")
        if len(str(new_pin)) != 4:
            raise ValueError("Пин должен содержать 4 символа")

        self.pin = new_pin
        print('Pin has been changed!')


if __name__ == "__main__":
    doctest.testmod()
