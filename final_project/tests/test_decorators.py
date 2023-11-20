import time
import re
from ..decorators import log, random_delay


def test_log_decorator(capfd):
    @log()
    def test_function():
        time.sleep(2)

    test_function()
    out, err = capfd.readouterr()
    expected_pattern = r'Выполнили за 2\.\d+ секунд!!'

    assert re.match(expected_pattern, out)

    @log('Все готово!')
    def test_function():
        time.sleep(2)

    test_function()
    out, err = capfd.readouterr()
    assert out.strip() == 'Все готово!'


def test_random_delay_decorator():
    @random_delay
    def test_function():
        return

    start = time.time()
    test_function()

    assert time.time() - start >= 1
