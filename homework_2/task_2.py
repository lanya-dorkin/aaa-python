import sys
import datetime
from typing import Callable, Any


def timed_output(function: Callable) -> Callable:
    original_write = sys.stdout.write

    def my_write(string_text: str) -> int | None:
        # без обработки переноса строки выдает гадость
        if string_text == '\n':
            return

        timestamp = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        return original_write(f'{timestamp}: {string_text}')

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sys.stdout.write = my_write

        result = function(*args, **kwargs)

        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name: str) -> None:
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
