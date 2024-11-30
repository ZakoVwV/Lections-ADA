"""
SOLID - Это набор из пяти принципов, объектно ориентированного программирования, которые были созданы для написсания гибкого, поддерживаемого кода.
"""

"""
S(SRP - Single Responsibility Principle) - Приницп единой ответственности. У каждого класса должно быть только одно предназначение, класс должен выполнять только один задачу
"""
# before
class ExportCsv:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    def prepare(self, raw_data):
        result = ''
        for data in raw_data:
            new_line = f"{data['name']}, {data['last_name']}\n"
            result += new_line
        return result
    
    def prepare(self, raw_data):
        result = ''
        for data in raw_data:
            new_line = f"{data['name']}, {data['last_name']}\n"
            result += new_line
        return result
    
    def write(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data)
    def write(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data)





#after

class FotmatData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self, raw_data):
        result = ''
        for data in raw_data:
            new_line = f"{data['name']}, {data['last_name']}\n"
            result += new_line
        return result
    


class FileWriter:
    
    def __init__(self, filename):
        self.filename = filename

    def write(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data)


"""
O (OCP - open-closed principle) - Принциа открытости-закрытости, класс должен быть открыт для расширения но не для модификации
"""

# before
class Diccount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'default':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
        
    

# after

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        if self.customer == 'default':
            return self.price * 0.2
        
class VIPDicsount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
    

class StaffDiscount(Discount):
    def get_discount(self):
        return super().get_discount() - 100
    


"""
L (LSP Liskov substitution priciple/Принцип подстановки Лисков) - объекты дочерних классов должны быть взаимосвязаными с объектами родительских классов
"""

# before
class Bird:
    def fly(self):
        return 'I can fly'

class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly")
    
bird1 = Bird()
bird2 = Ostrich()

def get_fly(bird_obj):
    return bird_obj.fly()

# print(get_fly(bird1))
# print(get_fly(bird2))

'''
Этот пример нарушает принцип подстановки лисков, так как ostrich это птица, но она не умеет летать, что нарушает общую логику и ожидаемое поведние
'''

# after

class Bird:
    def move(self):
        return 'Я могу летать'
    
class Sparrow(Bird):
    ...


class Ostrich(Bird):
    def move(self):
        return 'Я не умею летать, я умею бегать'
    

bird1 = Bird()
bird2 = Ostrich()
bird3 = Sparrow()

def get_move(bird_obj):
    return bird_obj.move()

print(get_move(bird1))
print(get_move(bird2))
print(get_move(bird3))

# Я могу летать
# Я не умею летать, я умею бегать
# Я могу летать



"""
I (ISP - Interface Segregation Principle/Принцип разделения интерфейса) - Не заставляйте классы реализовывать интерфейсы которые им не нужны/которые они не используют
"""

# before
class Worker:
    def eat(self):
        return 'eating food'
    
    def work(self):
        return 'working'



class RobotWOrker(Worker):
    def eat(self):
        return 'eating'
    
    def work(self):
        return 'working'
    

class HumanWorker(Worker):
    ...

class LazyWorker(Worker):
    def eat(self):
        return 'люблю хавать не буду работать'

robot1 = RobotWOrker()
print(robot1.work())
print(robot1.eat())

# after

class Workable:
    def work(self):
        return 'working'
    

class Etable:
    def eat(self):
        return 'eating food'
    

class RobotWOrker(Workable):
    def eat(self):
        return 'eating'
    
    def work(self):
        return 'working'
    

class HumanWorker(Etable, Workable):
    ...

class LazyWorker(Etable):
    def eat(self):
        return 'люблю хавать не буду работать'
    
lazy_boy = LazyWorker()
print(lazy_boy.eat())
# print(lazy_boy.work()) 

"""
D (DIP - Dependency Inversion Principle/Принцип инверсии зависимостей) - Модули верхних уровней не должны зависеть от модулей нижних уровней, модули от абстракций, а не от реализаций
"""

# before
class FileManager:
    def save_to_file(self, data):
        with open('file.txt', 'a') as file:
            file.write(data)


class DataProcessor:
    def process(self):
        data = 'some data'
        file_manager = FileManager()
        file_manager.save_to_file(data)

# after

# Абстракция
class Storage:
    def save(self, data):
        ...

# Конкретные реализаций
class FileManager(Storage):
    def save(self, data):
        return f'Save data: {data} in the box ;)'

class DatabasManager(Storage):
    def save(self, data):
        return f'Save data: {data} in data base'
    

file1 = FileManager()
db = DatabasManager()

print(file1.save('hello file storage'))
print(db.save({'name': 'Amir', "city": 'Bishkek'}))