# Запуск тестов

Запуск комманд производится из корневой директории. pytest должен быть установлен 

## Модуль pizza

    >>> pytest tests/test_pizza.py -v > tests/test_pizza_result.txt
    Тест запустится, и результат появится в файле tests/test_pizza_result.txt

## Модуль decorators

    >>> pytest tests/test_decorators.py -v > tests/test_decorators_result.txt
    Тест запустится, и результат появится в файле tests/test_decorators_result.txt.txt