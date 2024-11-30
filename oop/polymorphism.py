"""
Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная

"Один интерфейс - много реализаций"
"""


class Dog:
    def speak(self):
        print('Гав')

class Cat:
    def speak(self):
        print('Мяу')

class Frog:
    def speak(self):
        print('Ква')

obj = [Frog(), Cat(), Dog()]

for x in obj:
    x.speak()

# __add__ (+) - полиморф
print(5 + 5)
print('hello' + 'world')
print('5' + '5')
print([1,2,3,4] + [5,6,7])
a = [1, 2, 4, 5]
b = [4, 4, 4]
print(a.__add__(b))

# функция полиморф -> len(): __len__
print(len('hello'))
print(len([1, 2, 3]))
print(len({1: 1, 2: 2}))
print('abc'.__len__())

from math import pi


class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return f'Я фигура в двумерной плоскости: {self.name}'
    
class Square(Shape):
    def __init__(self, length):
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return super().fact() + '\nУ квадрата все стороны равны и углы равны 90 градусов' 


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Окружность')   
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2) 


kvadrat = Square(8)
Okr = Circle(3)

print(kvadrat.area())
print(kvadrat.fact())
print()
print(Okr.area())
print(Okr.fact())