"=======================================JSON=============================================="
# Javascript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

"""
Сериализация - Перевод с python объктов в JSON строку

Десереалезация - перевод из JSON строки в python объекты
"""

import json

"""
.dumps() - это метод сериализаций в json строку

.dump() - метод для сериализаций в json файл
"""

user_data = {
    'email': 'amir@gmail.com',
    'password':' 123',
    'is_active': False,
    'access': None
}

with open ('files/user_data.json', 'w') as file:
    json.dump(user_data, file)


json_string = json.dumps(user_data)
print(f'Json строка: {json_string}')

"""
loads() - метод для десериалезаций с json строки

load() - метод для десериалезаций с json файла
"""

with open('files/user_data.json', 'r') as file:
    python_data = json.load(file)
    print(f'{python_data} Десереализация')

python_dict = json.loads(json_string)
print(python_dict, 'С json строки')