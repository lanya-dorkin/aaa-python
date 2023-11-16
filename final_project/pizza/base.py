class Pizza:
    """
    Основной класс Pizza

    Атрибуты:
        size (str): Размер
        baked (bool): Готовность
        handled (bool): Статус
        _possible_size (set): Возможные размеры

    Методы:
        __init__: Инициализирует объект класса Pizza с заданным размером
        dict: Возвращает словарь с ингредиентами пиццы
        __str__: Возвращает строковое представление объекта пиццы
        __eq__: Сравнивает два объекта класса Pizza на равенство
    """

    _possible_size = set(["S", "M", "L", "XL"])

    def __init__(self, size: str = "L") -> None:
        """
        Инициализирует объект класса Pizza с заданным размером

        Аргументы:
            size (str): Размер пиццы. По умолчанию 'L'

        Исключения:
            ValueError: Невозможно создать пиццу с указанным размером
        """
        if size not in self._possible_size:
            msg = f"Invalid size. Please use on of {self._possible_size}."
            raise ValueError(msg)
        self._size = size
        self._baked = False
        self._handled = False

    @property
    def size(self) -> str:
        """Получает размер пиццы"""
        return self._size

    @property
    def baked(self) -> bool:
        """Получает статус выпечки пиццы"""
        return self._baked

    @property
    def handled(self) -> bool:
        """Получает статус обработки пиццы"""
        return self._handled

    @baked.setter
    def baked(self, new_status: bool) -> None:
        """Устанавливает статус выпечки пиццы

        Аргументы:
            new_status (bool): Новый статус выпечки
        """
        if self.baked:
            msg = "Already baked. Cannot be baked twice!"
            raise ValueError(msg)
        self._baked = new_status

    @handled.setter
    def handled(self, new_status: bool) -> None:
        """
        Устанавливает статус обработки пиццы

        Аргументы:
            new_status (bool): Новый статус обработки
        """
        if self.handled:
            msg = "Already handled :)"
            raise ValueError(msg)
        self._handled = new_status

    def dict(self) -> dict:
        """Возвращает словарь с ингредиентами пиццы"""
        return {ingredient: "1 штука" for ingredient in self.recipe}

    def __str__(self) -> str:
        """Возвращает строковое представление объекта пиццы"""
        return f"{self.name} {self.emoji}: {", ".join(self.recipe)}"

    def __eq__(self, other) -> bool:
        """Сравнивает два объекта класса Pizza на равенство"""
        if not isinstance(other, Pizza):
            raise TypeError("Cannot compare different types")

        name_eq = self.name == other.name
        size_eq = self.size == other.size
        recipe_eq = set(self.recipe) == set(other.recipe)

        return all([name_eq, size_eq, recipe_eq])
