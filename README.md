# Final_project_Chitai_gorod


## Шаблон для автоматизации тестирования на python

### Стек:
- pytest
- selenium
- requests
- allure
- config


### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore] (https://www.toptal.com/developers/gitignore)

### шаги по работе с проектом
- как получить токен для проекта
- как склонировать проект(гит клон)
- установить зависимости
- запуск тестов: 
pytest --alluredir=allure_results - запуск сразу всех тестов;
pytest tests/test_api.py --alluredir=allure-results - запуск Api тестов;
pytest tests/test_ui.py --alluredir=allure-results - запуск Ui тестов.

### Структура проекта

### Ссылка на проект и краткое описание 
- апи- такие то проверки
- юай тесты такие то проверки

### Библиотеки
- pip install pytest
- 

### Шаги:
1. Склонировать проект 'git clone https://github.com/KatrinAlex15/Final_project_Chitai_gorod.git'
2. Установить все зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет  'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'