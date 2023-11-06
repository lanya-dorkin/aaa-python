Шаги для запуска:
1. Переместиться в нужную директорию: 
    cd issue-04
2. Добавить текст команды в result.txt: 
    '> python -m pytest -v test_one_hot_encoder.py' > result.txt
3. Испольнить файл с тестами test_one_hot_encoder.py с помощью модуля pytest, направив результат в result.txt: 
    python -m pytest -v test_one_hot_encoder.py >> result.txt