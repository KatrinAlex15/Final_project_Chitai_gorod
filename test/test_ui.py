import pytest
from selenium import webdriver
import requests
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from page.main_page import MainPage

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicity_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()
   
def test_change_city(browser):
    main_page = MainPage(browser)




#поиск по полному названию книги на кириллице/латинице
#поиск по названию со знаками препинания
#поиск с путым запросом
#поиск несуществующей книги(абракадабра)
#поиск по автору
    
    
    
   
