#класс апи пейдж
import allure
import requests

#get_headers метод возвращает "Authorization": f"Bearer {self.token}"
class ApiPage:
    def __init__(self, url: str, token: str):
        #урл для доступа к апи
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }


#поиск по фразе
    def search_book(self, search_phrase):
        my_params={
            "phrase": search_phrase
        }

        resp = requests.get(self.url +'api/v2/search/product', headers=self.headers, params=my_params)
        return resp

#метод обраюотка результатов поиска: список книг из тела ответа