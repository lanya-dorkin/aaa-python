Шаги для запуска:
1. Переместиться в нужную директорию: 
    cd issue-02
2. Добавить текст команды в result.txt: 
    '> python -m pytest -v test_morse.py' > result.txt
3. Испольнить файл с тестами test_morse.py с помощью модуля pytest, направив результат в result.txt: 
    python -m pytest -v test_morse.py >> result.txt