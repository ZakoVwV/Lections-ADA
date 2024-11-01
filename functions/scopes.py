"=============================Область видимости============================="
# LEGB - Logal EGlobalnclosed Global Built-in

"=============================Built-in===================================="
# Встроенная область видимости (list, sum, dict, input ... )

"=============================Global============================="
# Все переменные которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные, можно использовать функцию globals()

# a = 10
# b = 12
# print(globals())
"==============================Local============================="
# Локальное пространство имен - те переменные, которые были созданы внутри функций

abc = 10
def func(a, b):
    print('GLOBALS', globals())
    hello = 'hello'
    print('LOCALS', locals())
    print(a, b, hello)
    print(abc)

# func(5, 7)
# print(hello) NameError: name 'hello' is not defined.

"===============================Enclosed================================"
# Замкнутое пространство имен - локальное пространство, у которого есть внутреннее локаотное пространство

# var = 'global'

# def func():
#     # локальное пространство имен для глобального пространства
#     # замкнутое пространство (потому что есть более локальное пространство)
#     var = 'enclosed'
#     def inner_func():
#         # локальное простарнство имен для пространства func
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()

# print(var)
# func()


# count = 1

# def increase_count():
#     global count
#     print(count)
#     count += 1

# increase_count()
# print(count)

# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter # это дает нам доступ на изменение переменной замкнутого пространства
#         print(counter)
#         counter += 1
#     for _ in range(i):
#         increase_counter()

# count(5)

# count = 5

# for i in range(1000):
#     print(count)
#     count += 1

# def main():
#     numbers = set()
#     for i in range(5):
#         num = float(input(f"Введите число {i + 1}: "))
#         numbers.add(num)
    
#     min_number = min(numbers)
#     print(f"Самое маленькое число, которое вы ввели: {min_number}")

# if __name__ == "__main__":
#     main()

# def procent():
#        a = int(input('Введите сумму: '))
#        if a < 100000:
#              raise Exception('Сумма не должна быть меньше 100 000')
#        print((a*(7,89/100)))
# procent()

# def num():
#     a = (input('Введите текст с цифрами:'))
#     for c in a:
#         if c.isdigit():
#             print(c)
#         else:
#             ' '
# num()

# def age():
#     years = int(input('Введите количество годов: '))
#     months = int(input('Введите количество месяцов: '))
#     days_years = (12 * 30 * years)
#     days_monhts = (30 * months)
#     print(days_years + days_monhts)
# age()

# def add(a, b):
#     print(a + b)
# add(5, 10)

# def get_string_length(str):
#     print(int(len(str)))
# get_string_length('hello')

# def get_type(a, b):
#     print(type(a))
#     print(type(b))
# get_type(True, 'hello')

# def check(a):
#     if a % 2 == 0:
#         print('It is even number')
#     else:
#         print('It is odd number')
# check(971409579023876023702967)

# def is_palindrome(text):
#     return text == text[::-1]
# is_palindrome('казак')


# def max_num(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# max_num(5, 11)

# import math
# def multiply_list():
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(math.prod(list))
# multiply_list()

# def sum_digits(n):
#     if (n==0):
#         return 0
#     else:
#         return n%10+sum_digits(n//10)
# print(sum_digits(12345))


