import time
import random
from typing import Callable, Any


def random_delay(func: Callable) -> Callable:
    """
    Декоратор добавляет случайную задержку перед вызовом функции

    Аргументы:
        func (callable): Функция, к которой применяется декоратор

    Возвращает:
        callable: Обернутая функция с добавленной случайной задержкой
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обернутая функция с задержкой."""
        delay_time = random.uniform(1, 3)
        time.sleep(delay_time)
        return func(*args, **kwargs)

    return wrapper
