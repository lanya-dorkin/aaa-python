import sys
import datetime


original_write = sys.stdout.write


def my_write(string_text: str) -> int | None:
    # без обработки переноса строки выдает гадость
    if string_text == '\n':
        return

    timestamp = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    return original_write(f'{timestamp}: {string_text}')


sys.stdout.write = my_write


if __name__ == '__main__':
    print('1, 2, 3')
