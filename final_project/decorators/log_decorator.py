import time
from functools import wraps


def log(template='Выполнили за {} секунд!!'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = round(time.time() - start_time, 2)
            print(template.format(execution_time))
            return result
        return wrapper
    return decorator
