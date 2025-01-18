## Final_project_Chitai_gorod

## Проект "Final_project_Chitai_gorod" представляет собой набор автоматизированных тестов для проверки функциональности веб-приложения (интернет магазин книг), реализованных с использованием Selenium и pytest. ДЛя визуализации отчетов используется Allure. 


### Стек:
- pytest
- selenium
- requests
- allure
- config

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Веб-интерфейс сервиса](https://www.chitai-gorod.ru/)

### Структура проекта
- **page**: 
   - `api_page.py`: код для взаимодействия с API сайта
   - `main_page.py`: код для взаимодействия с  основной страницей сайта
- **test**:
   - `test_ui.py`: тесты пользовательского интерфейса
   - `test_api.py`: тесты API
- **.gitignore**: файл, который игнорируется при  Git-контроле
- **config.py**: конфигурационный файл 
- **pytest.ini**: конфигурационный файл для фреймворка тестирования pytest
- **requirements.txt**: файл, который содержит список зависимостей проекта
- **README.md**: файл с описанием проекта 

### Ссылка на проект и краткое описание 
https://kate-alex.yonote.ru/doc/kursovaya-rabota-3-UlKN4by0ZZ

- тесты API (test_api.py): тесты для проверки функциональности API (поиск книг по автору на латинице/кириллице, поиск с пустым запросом, получение информации о книге по нажатию на нее)
- тесты UI (test_ui.py): позитивные и негативные тесты для проверки пользовательского интерфейса, выбор города нахождения, проверка недоступных для заказа книг. 

### Шаги по работе с проектом
1. Склонировать проект `git clone https://github.com/KatrinAlex15/Final_project_Chitai_gorod.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Получить токен и прописать его в файле `config.py`
3. Запустить тесты:
```python
pytest --alluredir=allure-files - запуск сразу всех тестов;
pytest tests/test_api.py --alluredir=allure-files - запуск Api тестов;
pytest tests/test_ui.py --alluredir=allure-files - запуск Ui тестов.
```
4. Сгенерировать отчет  `allure generate allure-files --clean -o allure-report`
5. Открыть отчет `allure open allure-report`
