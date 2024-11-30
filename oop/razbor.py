# ООП
"""
ООП - объектно ориентированое порграммирование, парадигма
1) Наследование (Основной)
2) Инкапсуляция (Основной)
3) Полиморфизм (Основной)

4) Абстракция
5) Ассоциация
"""

"""
1) Наследование - Принцип ООП, который позволяет одному классу наследовать аттрибуты и методы другого класса
2) Инкапсуляций - Принцип ООП, у которого есть 2 трактовки:
    1) класс является некой капсулой в которой хранятся все аттрибуты и методы
    2) Режимы доступа (Публичный, защищенный, приватный)
3) Полиморфизм - принцип ООП, в котором когда у нас метод называется одиннаково но выполняет разный функционал (Один интерфейс - много реализаций)

4) Абстракция - Принцип ООП, в котором мы создаем класс пустышку от которого наследуются дочерние классы, и переопределяют его методы (Нужен для правильности полиморфизма), абстракция обязует нас переопределять все методы, на которых был декоратор @absctractmethod, если метод не переопределить то выйдет ошибка
5) Ассоциация - Принцип ООП, в котором два класса связаны друг с другом, есть два вида связи:
    1) агрегация - слабая
    2) композиция - сильная связь
"""

# class Battery:
#     power = 100

#     def charge(self):
#         if self.power < 100:
#             self.power = 100

# class iPhone:
#     def __init__(self, color):
#         self.color = color
#         self.battery = Battery() # Композиция

    # def __init__(self, color, battery):
    #     self.color = color
    #     self.battery = battery # Агрегация

# battery = Battery()

# iphone = iPhone('blue', 'black')
# print(iphone.battery,power)
# del iphone
# print(iphone.battery.power)
# del iphone
# print(battery)
# print(iphone)


# 1.  Создайте класс Product с атрибутами:
#  • base_price: базовая цена продукта (20000).
#  • model, year, color: аттрибуты экземпляра класса.
#  Реализуйте методы:
#  • has_garanty(year): проверяет гарантию (действует 2 года), возвращает текст о ее состоянии.
#  • change_price(rate): увеличивает base_price на указанный процент.
#  Пример: Создать продукт, повысить цену на 2%, проверить гарантию
# obj.change_price(2)
# print(obj.has_garantiya(2010))
# print(obj.base_price)

class Product:
    base_price = 20000

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def has_garanty(self, year):
        past_year = year - self.year
        if past_year > 2:
            return f'Гарантия на этот товар истекла'
        return 'Гарантия действительна'
        
    @classmethod
    def change_price(cls, rate):
        inflation = round(cls.base_price * (rate/100))
        cls.base_price += inflation


# 2. Создайте класс User с атрибутами: (static-class methods)
#  • name, lastname, email.
#  Реализуйте методы:
#  • validate_email(email): проверяет, содержит ли email символ @.
#  • __str__(): возвращает данные пользователя или сообщение о неверном email.
#  • create_user(data): создает пользователя из строки "Имя, Фамилия, email".

class User:
    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email


    @staticmethod
    def validate_email(email: str) -> bool:
        return '@' in email and '.' in email[email.index('@'):]
    
    def __str__(self):
        if self.validate_email(self.email):
            return f'{self.name} - {self.email}'
        return f'Ваш email адрес не валиден'

    @classmethod
    def create_user(cls, data):
        user_info = data.split(',') # ['name', 'last_name', 'email']
        name = user_info[0]
        last_name = user_info[1]
        email = user_info[2]
        user = cls(name, last_name, email)
        return user

user1 = User.create_user('nikita, grebnev, n@.com')
print(user1)



# person1 = User('nikita', 'grebnev', 'grebnev@gmail.com')
# person2 = User.create_user('nikia, grebnev, grebnev@gmail.com')



# 3. Создайте класс ADA с атрибутами: (classmethod)z
#  • student_count: количество студентов.
#  • name, language, kpi: параметры студента.
#  Реализуйте методы:
#  • new_student(name, language, kpi): создает нового студента и увеличивает счетчик.
#  • get_info(): возвращает данные студента.
#  • set_kpi(kpi): устанавливает новый kpi.
#  Пример: Создать двух студентов, обновить их kpi, вывести данные и общее число студентов.

class ADA:
    student_count = 0

    def __init__(self, name, language, kpi):
        self.name = name
        self.language = language
        self.kpi = kpi

    @classmethod
    def new_student(cls, name, language, kpi):
        cls.student_count += 1
        student  = cls(name, language, kpi)
        return student
    
    def get_info(self):
        return f'{self.name} - language:{self.language}, kpi: {self.kpi}'
    

    def set_kpi(self, kpi):
        self.kpi = kpi
        return self.kpi
    
Student1 = ADA.new_student('nikita', 'python', 2.0)
Student2 = ADA.new_student('Tima', 'python', 5.0)

print(Student1.set_kpi(10.0))
print(Student2.set_kpi(8.0))

print(Student1.get_info())
print(Student2.get_info())

print(ADA.student_count)


# 4. Создайте класс Bike с атрибутами:
#  • cost, make, model, year: себестоимость, производитель, модель, год.
#  • _sale_price, sold, min_profit: цена продажи, статус продажи, минимальная прибыль.
#  Реализуйте методы:
#  • set_cost(cost): устанавливает цену продажи с учетом минимальной прибыли.
#  • service(price): увеличивает цену продажи.
#  • sell(): меняет статус на “продано”, возвращает прибыль.
#  • get_default_bike(): создает велосипед с параметрами по умолчанию.
#  Пример: Создать стандартный велосипед, установить себестоимость, добавить обслуживание, продать.

class Bike:
    def __init__(self, cost, make, model, year, sale_price, min_profit):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self._sale_price = sale_price
        self.sold = False
        self.min_profit = min_profit

    def set_cost(self):
        self._sale_price += self.min_profit
        return self._sale_price
    
    def service(self, price):
        self._sale_price += price
        return self._sale_price
    
    def sell(self):
        if self.sold:
            return 'Данный товар продан'
        self.sold = True
        return f'Прибыль: {self._sale_price - self.cost}'
    
    @classmethod
    def get_default_bike(cls):
        return cls(10000, 'Giant', 'A123', 2024, 20000, 2000)
    
bike = Bike.get_default_bike()
    

print(bike.set_cost())
print(bike.service(2000))
print(bike.sell())


# 5. Создайте класс MoneyFmt с атрибутом:
#  • amount: денежная сумма.
#  Реализуйте методы:
#  • update(amount): обновляет сумму.
#  • __repr__(): возвращает сумму как строку.
#  • dollarize(float_num): форматирует число в денежный вид (например, $1,234.56).
#  • __str__(): возвращает отформатированную сумму.
#  Пример: Создать объект с суммой, обновить ее, проверить формат с отрицательным значением, вывести с помощью repr().

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, amount):
        self.amount = amount

    def __repr__(self):
        return str(self.amount)    

    @staticmethod
    def dollarize(float_num):
        return f'${float_num:,.2f}'.replace("$-", "-$")

    def __str__(self):
        return MoneyFmt.dollarize(self.amount)
        

obj1 = MoneyFmt(-14007785576597656.00)
print(obj1)
obj1.update(-23235262263.2446374)
print(obj1)
print(repr(obj1))