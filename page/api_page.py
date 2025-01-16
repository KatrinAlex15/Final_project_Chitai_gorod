#класс апи пейдж
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure

#get_headers метод возвращает "Authorization": f"Bearer {self.token}"
class ApiPage:
    def __init__(self, __url: str, token: str):
        #урл для доступа к апи
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }


#поиск книги 
    def search_book(self, search):
        resp = requests.get(self.url)

#метод обраюотка результатов поиска: список книг из тела ответа