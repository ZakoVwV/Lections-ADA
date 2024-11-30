"""
Магические методы (dunder(double underscore) methods) - (__init__, __str__, __add__, __eq__,__new__ и,т,д)
Магия в том, что эти методы вызыаются без прямого обращения к ним, некторые методы отвечают за определенные операторы
"""

# class A:
#     pass

# print(dir(A))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# # __init__ - метод для того чтобы присвоить объекту аттрибуты экземпляра, он вызывается самостоятельно при создании объекта

class Human:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.name} {self.last_name}'
    

Nikita = Human('nikita', 'grebnev')
# print(Nikita)

# # __new__ - магичесский метод, который отвечает за создание нового объекта, он отрабатывает без вызова, и отрабатывает перед методом __init__

# # Singleton - от класса можно создать только один объект

class Singleton:
    _instance = None

    def __new__(cls): # cls - ссылка на класс
        if not cls._instance: # если объект еще не создан
            cls._instance = super().__new__(cls) # то мы вызываем родительский метод, и создаем новый экземпляр
        return cls._instance # в ином случае, если объект уже есть, то возвращаем его


# s1 = Singleton()
# s2 = Singleton()
# print(s1)
# print(s2)
# print(s1 is s2)

# __add__ - магический метод, который отвечает за сложение

'5' + '5'
print('5'.__add__('5')) # 55

# __hash__ - магический метод, который отвечает за хаширование данных

print(hash('234234')) # 7994014370630214006
('aaa'.__hash__()) # 212415611372320013

# __dict__ - он возвращает все аттрибуты у объекта

print(Nikita.__dict__) # {'name': 'nikita', 'last_name': 'grebnev'}

# __eq__ - (equal) - знак равенства
a = 6
b = 7

print(6 == 6)
print(a.__eq__(b))

# __lt__ - знак меньше (last than)
print(a < b)




