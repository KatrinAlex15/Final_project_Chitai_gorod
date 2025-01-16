from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config import UI_BASE_URL



class MainPage:

    #Настроить браузер, перейти на сайт
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(UI_BASE_URL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, ".button.change-city__button.blue").click()    

    #Поменять город
    def change_city(self, change_city) -> None:
        self.driver.find_element(By.CSS_SELECTOR, ".header-city.header-top-bar__city").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button.change-city__button.light-blue").click()
        self.driver.find_element(By.XPATH, f"//li[text(={change_city})]").click()

    # поиск
    def enter_search_query(self, query):
        self.driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
     
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

    
