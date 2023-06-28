import requests                                                     # Importing "requests" library for requests|Импорт библиотеки "Запросы" для отправки запросов
import json                                                         # Importing "json" library for work with JSON|Импорт библиотеки "JSON" для работы с JSON

print('Pokemon is...')                                              # Information displayed to the user (what should he enter)|Информация, отображаемая пользователю (что он должен ввести)
print('(Can be used name or ID)')                                   # Information displayed to the user (explanation)|Информация, отображаемая пользователю (пояснение)

Search = input(str())                                               # Input pokeName/pokeID|Ввод имени покемона/айди покемона
URL = ('https://pokeapi.co/api/v2/pokemon/'+Search)                 # Pokeapi link + input|Ссылка на pokeapi + введённые данные
response = requests.get(URL)                                        # Request by URL (get)|Запрос по переменной URL (get)
    
data = json.loads(response.text)                                    # Getting response information like data block|Получение данных ответа как блок данных
    
id_card = data['id']                                                # Getting 'id' data|Получение данных 'id'
name = data['name']                                                 # Getting 'name' data|Получение данных 'name'
height = data['height']                                             # Getting 'height' data|Получение данных 'height'
weight = data['weight']                                             # Getting 'weight' data|Получение данных 'weight'

print('ID:', id_card)                                               # Printing ID data|Вывод данных ID
print('Name:', name)                                                # Printing name data|Вывод данных name
print('Height:', height)                                            # Printing height data|Вывод данных height
print('Weight:', weight)                                            # Printing weight data|Вывод данных weight
URL = 'https://pokeapi.co/api/v2/pokemon/1'
h = requests.head(URL)
header = h.headers
length = header.get('Content-Length')
print(length)