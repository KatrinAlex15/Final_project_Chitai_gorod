from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config import UI_URL



class MainPage:

    #Настроить браузер, перейти на сайт
    def __init__(self, driver: WebDriver):
        self._driver: WebDriver = driver
        self._driver.get(UI_URL)
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

       

        #self.__url = "https://www.chitai-gorod.ru/"
        #self.__driver = driver

    #Перейти на страницу "Читай город"
    #def go(self):
        #self.__driver.get(self.__url)

    #Поменять город
    def change_city(self, change_city) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, ".header-city.header-top-bar__city").click()
        self.__driver.find_element(By.CSS_SELECTOR, ".button change-city.light-blue").click()
        self.__driver.find_element(By.XPATH, f"//li[text(={change_city})]").click()

    #строка поиска
    def enter_search_query(self, query):
        search_input = self.__driver.find_element(By.CSS_SELECTOR, ".header-search__input")
        search_input.send_keys(query)

        #нажать searh button кнопки поиска
    def click_searh_button(self, button):
        button = driver.find_element(By.CSS_SELECTOR, ".header-search__input")
        button.click()
     #получение результатов поиска
    def find_book(self, value: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(value + Keys.RETURN)

#проверка сообщения об отсутствии резутаттов (рапрпарпр)
    def check_result(self) -> list[str]:
         self.__driver.find_element(By.CSS_SELECTOR, ".catalog-empty-result__header")
    
        
    def check_result(self) -> list[str]:
        #ожидаем загрузки результатов поиска
        (WebDriverWait(self.__driver,10).
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".catalog-empty-result__header"))))
        self.__driver.find_element(By.CSS_SELECTOR, ".catalog-empty-result__header")
       
    
    #проверка поиска по автору, проверить корректность проверки ожмдаемых авторов
    def serch_authors(self) -> list[str]:
        self.__driver.find_element(By.CSS_SELECTOR, ".search-page__found-message")
        
    #

    
