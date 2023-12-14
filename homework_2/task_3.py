import sys
from typing import Callable, Any


def redirect_output(filepath: str) -> Callable:

    def decorator(function: Callable) -> Callable:
        original_stdout = sys.stdout

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with open(filepath, 'a') as file:
                sys.stdout = file
                result = function(*args, **kwargs)

            sys.stdout = original_stdout
            return result

        return wrapper

    return decorator


@redirect_output('./function_output.txt')
def calculate() -> None:
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
