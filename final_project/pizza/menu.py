from .base import Pizza
from .pizzas import Margherita, Pepperoni, Hawaiian, Barcelona, Myasnaya


class Menu:
    """Класс Menu представляет меню пиццерии

    Атрибуты:
        default_mapping (dict): Словарь по умолчанию,
            представляющий собой соответствие имени пиццы классу пиццы
        default_title (str): Заголовок меню по умолчанию
        choice (list[str]): Список доступных вариантов пиццы в меню

    Методы:
        __init__: Инициализирует объект класса Menu с меню и заголовком
        display: Возвращает строковое представление меню
        __getitem__: Получает объект пиццы по имени из меню
    """

    default_mapping = {
        'margherita': Margherita,
        'pepperoni': Pepperoni,
        'hawaiian': Hawaiian,
        'barcelona': Barcelona,
        'myasnaya': Myasnaya,
    }
    default_title = 'МЕНЮ НАШЕЙ ЗАМЕЧАТЕЛЬНОЙ ПИЦЦЕРИИ:'

    def __init__(self, menu: dict = None, title: str = None) -> None:
        """Инициализирует объект класса Menu

        Аргументы:
            menu (dict, optional): Меню пиццерии, где ключ - имя пиццы,
                значение - класс пиццы
            title (str, optional): Заголовок меню
        """
        self._mapping = menu if menu is not None else self.default_mapping
        self._title = title if title is not None else self.default_title

    @property
    def choice(self) -> list[str]:
        """Возвращает список доступных вариантов пиццы в меню"""
        return list(self._mapping.keys())

    def display(self) -> str:
        """Возвращает строковое представление меню"""
        menu = [self._title]
        menu.extend([str(pizza()) for pizza in self._mapping.values()])
        return '\n'.join(menu).strip()

    def __getitem__(self, name: str) -> Pizza:
        """Получает объект пиццы по имени из меню

        Аргументы:
            name (str): Имя пиццы

        Возвращает:
            Pizza: Объект пиццы

        Исключения:
            ValueError: Пиццы с указанным именем нет в меню
        """
        result = self._mapping.get(name, None)
        if result is None:
            msg = f'Сегодня {name} не привезли!'
            raise ValueError(msg)
        return result
