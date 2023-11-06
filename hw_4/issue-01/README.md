Шаги для запуска:
1. Переместиться в нужную директорию: 
    cd issue-01
2. Добавить текст команды в result.txt: 
    '> python -m doctest -o NORMALIZE_WHITESPACE morse.py -v' > result.txt
3. Испольнить файл с кодом и тестами morse.py с помощью модуля doctest, направив результат в result.txt: 
    python -m doctest -o NORMALIZE_WHITESPACE morse.py -v >> result.txt