import json
from collections import UserDict, UserList
import keyword
from typing import Any


class AdFields(UserDict, UserList):
    """
    Класс AdFields наследуется от классов UserDict и UserList и представляет
    собой поля объявления с доступом к атрибутрам через точку.
    """
    def __init__(self, data: dict | list) -> None:
        """
        Принимает на вход данные в виде словаря или списка. Ключи и значения
        в нем преобразуются с помощью методов change_keyword и change_type.

        Параметры:
        data (dict или list): словарь или список с данными.
        """
        if isinstance(data, dict):
            data = {
                AdFields.change_keyword(key):
                AdFields.change_type(value) for key, value in data.items()
            }
            UserDict.__init__(self, data)
        elif isinstance(data, list):
            data = [
                AdFields.change_type(value) for value in data
            ]
            UserList.__init__(self, data)

    @staticmethod
    def change_type(value: Any) -> Any:
        """Преобразует тип данных из dict или list."""
        if isinstance(value, dict) or isinstance(value, list):
            return AdFields(value)
        return value

    @staticmethod
    def change_keyword(name: str) -> str:
        """Преобразует ключ в случае совпадения с ключевым словом."""
        if keyword.iskeyword(name):
            name += '_'
        return name

    def __getattr__(self, name: str) -> Any:
        return self.get(name)


class Advert:
    """
    Класс Advert представляет собой объявления с доступом к полям через точку
    и валидацией обязательных полей title и price.
    """
    def __init__(self, mapping: dict) -> None:
        """
        Принимает на вход данные в виде словаря.

        Параметры:
        mapping (dict): данные объявления. Обязательно содержит title,
            при наличии price, значение >= 0.
        """
        self.price = mapping['price'] if 'price' in mapping else 0
        self.mapping = AdFields(mapping)
        if self.mapping.get('title') is None:
            raise ValueError('title is required')

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> int:
        if value < 0:
            raise ValueError('must be >= 0')
        self._price = value

    def __getattr__(self, name: str) -> Any:
        return self.mapping.get(name)


if __name__ == '__main__':
    dog_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }"""
    dog_ad = json.loads(dog_str)
    dog_ad = Advert(dog_ad)
    print(dog_ad.title)
    print(dog_ad.price)
    print(dog_ad.class_)
