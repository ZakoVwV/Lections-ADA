"""
Абстракуция
"""

"""
Абстракуция - это принцип ООП, а котором создается абстрактный класс(класс - пустышка), в котором задаются названия аттрибутов и методов для того, чтобы мы могли их переопределить в дочерних классах 
У нам есть названия но нет логики
"""

from abc import ABC, abstractmethod


class AbstractAnimal(ABC):

    @abstractmethod
    def speak(self):
        print('voice')

# obj_ = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract method speak
"""
Создавать объект от абстрактного класса нельзя
"""

class Dog(AbstractAnimal):
    def speak(self):
        print('BARKBARKNARKBARKABRKBAKBARKBARKABRKBARKBARKBARK!')

obj1 = Dog()
obj1.speak()
"""
Абстракция нужна для правильности полиморфизма
@absractmethod - декоратор, который требует переопределения методы в дочернем классе
"""
from math import pi

class AbstractShape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        ...

class Square(AbstractShape):
    def __init__(self, length):
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2
    
    def fact(self):
        return f'Я фигура: {self.name}'
    
class Circle(AbstractShape):
    def __init__(self, radius):
        super().__init__('Окружность')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    
obj = Circle(5)
print(obj.area())
