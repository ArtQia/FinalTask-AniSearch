import requests                                                     # Importing "requests" library for requests|������ ���������� "�������" ��� �������� ��������
import json                                                         # Importing "json" library for work with JSON|������ ���������� "JSON" ��� ������ � JSON

print('Pokemon is...')                                              # Information displayed to the user (what should he enter)|����������, ������������ ������������ (��� �� ������ ������)
print('(Can be used name or ID)')                                   # Information displayed to the user (explanation)|����������, ������������ ������������ (���������)

Search = input(str())                                               # Input pokeName/pokeID|���� ����� ��������/���� ��������
URL = ('https://pokeapi.co/api/v2/pokemon/'+Search)                 # Pokeapi link + input|������ �� pokeapi + �������� ������
response = requests.get(URL)                                        # Request by URL (get)|������ �� ���������� URL (get)
    
data = json.loads(response.text)                                    # Getting response information like data block|��������� ������ ������ ��� ���� ������
    
id_card = data['id']                                                # Getting 'id' data|��������� ������ 'id'
name = data['name']                                                 # Getting 'name' data|��������� ������ 'name'
height = data['height']                                             # Getting 'height' data|��������� ������ 'height'
weight = data['weight']                                             # Getting 'weight' data|��������� ������ 'weight'

print('ID:', id_card)                                               # Printing ID data|����� ������ ID
print('Name:', name)                                                # Printing name data|����� ������ name
print('Height:', height)                                            # Printing height data|����� ������ height
print('Weight:', weight)                                            # Printing weight data|����� ������ weight
URL = 'https://pokeapi.co/api/v2/pokemon/1'
h = requests.head(URL)
header = h.headers
length = header.get('Content-Length')
print(length)