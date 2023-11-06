Шаги для запуска:
1. Переместиться в нужную директорию: 
    cd issue-03
2. Добавить текст команды в result.txt:
    'python -m unittest -v' > result.txt
3. Испольнить файл с тестами с помощью модуля unittest, направив результат в result.txt: 
    python -m unittest -v >> result.txt 2>&1