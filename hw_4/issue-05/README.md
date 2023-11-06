Шаги для запуска:
1. Переместиться в нужную директорию: 
    cd issue-05
2. Добавить текст команды в result.txt: 
    '> python -m pytest -v --cov . --cov-report html' > result.txt
3. Испольнить файл с тестами test_what_is_year_now.py с помощью модуля pytest, сгенерив отчет о покрытии в html и направив результат в result.txt: 
    python -m pytest -v --cov . --cov-report html >> result.txt