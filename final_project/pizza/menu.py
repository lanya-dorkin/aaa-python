from .base import Pizza
from .pizzas import Margherita, Pepperoni, Hawaiian, Barcelona, Myasnaya


class Menu:
    _mapping = {
        'margherita': Margherita, 
        'pepperoni': Pepperoni, 
        'hawaiian': Hawaiian, 
        'barcelona': Barcelona, 
        'myasnaya': Myasnaya
    }
    _title = 'МЕНЮ НАШЕЙ ЗАМЕЧАТЕЛЬНОЙ ПИЦЦЕРИИ:'

    def __init__(self, menu: dict = None, title: str = None):
        if menu is not None:
            self._mapping = menu
        if title is not None:
            self._title = title

    @property
    def choice(self) -> list[str]:
        return list(self._mapping.keys())
    
    def display(self) -> str:
        menu = [self._title]
        menu.extend([str(pizza()) for pizza in self._mapping.values()])
        return '\n'.join(menu)
    
    def __getitem__(self, name: str) -> Pizza:
        result = self._mapping.get(name, None)
        if result is None:
            msg = f'Сегодня {name} не привезли!'
            raise ValueError(msg)
        return result
