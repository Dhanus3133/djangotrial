import requests
import json
# response = requests.get('C:/Users/Dhanus/Downloads/Compressed/city.list.json/city.json')

# print(response.json())


with open('city.json', 'r', encoding="utf8") as f:
    data = json.load(f)
# print(data['main'])

with open('cities.py', 'w', encoding="utf8") as txt:
    # for x in data:
    #     print(x['name'], end=', ')

    list = [x['name'] for x in data]
    txt.write('cities =' + str(list))