from page.api_page import ApiPage
from config import API_URL, API_TOKEN
import requests


api = ApiPage(API_URL, API_TOKEN)

# поиск по фразе(книге)

def test_search_by_title():
    resp_search = api.search_book("мастер и маргарита")
    assert resp_search.status_code == 200
    assert "мастер и маргарита" in resp_search.text


#поиск по автору
def test_search_by_author():
    resp_search = api.search_book("пушкин")
    assert resp_search.status_code == 200
    assert "пушкин" in resp_search.text

#поиск с пустым запросом
def test_search_by_empty_string():
    resp_search = api.search_book("")
    assert resp_search.status_code == 400
    assert "Phrase обязательное поле" in resp_search.text
    
#поиск по автору на латинице
def test_search_by_author_in_english():
    resp_search = api.search_book("kant")
    assert resp_search.status_code == 200
    assert "kant" in resp_search.text




#получение информации о книге по нажатию на нее