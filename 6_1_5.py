# print("hello word!")
import requests
from pprint import pprint

#api_url = 'http://api.open-notify.org/iss-now.json'
api_url= 'http://numbersapi.com/43/'

# Отправляем GET-запрос и сохраняем ответ в переменной response
response = requests.get(api_url)

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код
