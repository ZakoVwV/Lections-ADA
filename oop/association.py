"""
Ассоциация - принцип ООП, в котором два класса связаны друг с другом. Связь обозначает то, что внутри одного объекта будет существовать другой объект от другого класса

ВИДЫ СВЯЗЕЙ:
Агрегация - слабая связь
Композиция - сильная связь
"""


# Пример с сильной связью (Композиция)


class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class iPhone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()
        # Когда мы создаем внутри класса объект от другого класса это композиция (сильная связь)


a = iPhone('Blue')
a.battery.power -= 50
print(a.battery.power)
a.battery.charge()
print(a.battery.power)
del a
# print(a) Name Error
# При удалений объкта от класса  iPhone, вместе с ним удаляется и батарейека


# Пример со слабой связью - Агрегация


class Nokia:
    def __init__(self, battery: Battery, color: str):
        self.color = color
        self.battery = battery
        # Когда объект создается из вне класса и передается внутрь, это - Агрегация

battery = Battery()

nokia1 = Nokia(battery, 'Black')
print(nokia1.battery.power)
nokia1.battery.power -= 50
print(nokia1.battery.power)
nokia1.battery.charge()
print(nokia1.battery.power)
nokia2 = Nokia(battery, 'Blue')
print(nokia2.battery.power)

# Пример с композицией

class wall:
    def __init__(self, direction):
        self.type = direction

    def __str__(self):
        return f'{self.type}'

class Room:
    def __init__(self):
        self.west_wall = wall('west')
        self.east_wall = wall('east')
        self.south_wall = wall('south')
        self.north_wall = wall('north')
    
obj = Room()
print(obj.west_wall)
print(obj.east_wall)
print(obj.north_wall)


# Композиция


class Engine:
    country = 'Germany'
    def __init__(self, power, type):
        self.power = power
        self.type = type
        

    def __str__(self):
        return f'Power: {self.power}'
    

class Audi:
    brand = 'Audi'
    country = 'Germany'

    def __init__(self, model, power, engine_type):
        self.engine = Engine(power, engine_type)
        self.model = model

    def __str__(self):
        return f'{self.brand} {self.model} -> Engine: {self.engine.type} -> engine country: {self.engine.country}'
    
car = Audi(model='Q8', power=500, engine_type='V8')
print(car)


