import time
from functools import wraps
from typing import Callable, Any


def log(template: str = "Выполнили за {} секунд!!") -> Callable:
    """Декоратор логирует время выполнения функции

    Аргументы:
        template (str, optional): Шаблон сообщения о времени выполнения
            По умолчанию 'Выполнили за {} секунд!!'

    Возвращает:
        callable: Обернутая функция с логированием времени выполнения
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обернутая функция с логированием времени выполнения"""
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = round(time.time() - start_time, 2)
            print(template.format(execution_time))
            return result

        return wrapper

    return decorator
