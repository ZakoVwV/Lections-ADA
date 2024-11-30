"""
В классах есть множество разных методова, мы знакомы с самыми распространеными, методы которые работают с конкретным экземпляром класса
Но, так-же в разработке часто используется такие методы как:
1) classmethods
2) staticmethods
"""

class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f'Hello {self.name}'
    
obj = User('Nikita')
print(obj.greet())


# classmethods - это методы которые работают не с объектом, а с самим классом, и создаются при помощи декоратора @classmethods, класс методы всегда первым аргументом принимает cls (ссылка на класс)

class User:
    default_role = 'user'

    def __init__(self, name, role=None):
        self.name = name
        self.role = role or User.default_role

    @classmethod
    def create_admin(cls, name): # это метод класса который создает объект с фиксированной роль. админа
        return cls(name, role='admin')
    
user = User('Alice')
print(user.name, user.role)

admin = User.create_admin('Nikita')
print(admin.name, admin.role)

import json

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(order_id=data['order_id'], items=data['items'])
    

json_data = '{"order_id": 1, "items": ["apple", "banana"]}'
order = Order.from_json(json_data)
print(order.order_id,order.items)

# staticmethod - независимые функций внутри класса
# это методы которые не принимают никаких ссылок в аргументы, и оги не зависят ни от объекта, ни от класса, зачастую применяются для каких-либо операций


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
print(MathUtils.add(7, 90))
print(MathUtils.multiply(7, 90))

class Product:
    tax_rate = 0.2 # налог 20%
    product_list = []

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def calculate_tax(price):
        return price + (price * Product.tax_rate)
    
iphone_obj = Product('iPhone 11', 1000)
price_with_tax = Product.calculate_tax(iphone_obj.price)
print(price_with_tax)

class Validator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return '@' in email and '.' in email[email.index('@'):]
    
print(Validator.is_valid_email('amir.zakov@mail.ru'))


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def create_guest(cls, username):
        return cls(username, 'guest')
    
    def __str__(self):
        return f'{self.role} - {self.username}'
    
user = User('nikita', 'user')
print(user)

guest = User.create_guest('anonym')
print(guest)