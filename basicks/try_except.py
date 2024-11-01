'=============================Exception=============================='
# Исследования (Ошибки) - объекты которые прерывают работу кода, если они не обработаны

# SyntaxError
# Исключение, которое которое выходит когда в коде допущена синтаксическая ошибка

# (
    # SyntaxError: '(' was never closed
# '  SyntaxError: unterminated string literal (detected at line 9)
# a = 

# NameError
# Исключение, которое выходит когда мы обращаемся к несуществующей переменной
# print(a)
# NameError: name 'a' is not defined

# IndexError
# Исключение, которое выходит, когда мы обращаемся к несуществующему индексу
# print(list1[1000]) # NameError: name 'list1' is not defined. Did you mean: 'list'?
# list2 = [1, 2, 3, 4]
# print(list2[1000]) #list index out of range

#KeyError
# Исклюсение, которое выходит по несуществующему ключу
# dict_ = {1: 321, 2: 2}
# print(dict_[1999]) #KeyError: 1999


# ValueError
# Исключение котрое возникает когда мы передаем в функцию неккоректный для нее тип данных
# print(int('pon'))
# когда мы распаковываем итерируемый объект на несколько переменных и количество переменных не совпадает с количеством элементов
# a, b = [1]

# IndetationError
# Выходит, когад мы неправильно используем отступ

    # a = 5 #  IndetationError: unexpected indent

# TypeError
"""
Когда мы пытаемся передать функций больше или меньше аргументов, чем принимает функция
"""
# for i in 123: #TypeError: 'int' object is not iterable
# '5' + 5 # TypeError: can only concatenate str (not "int") to str
#{[1,2,3]: 12} #TypeError: unhashable type: 'list'
# input('введи цифру', 1) # input expected at most 1 argument, got 2

# Exception
# Это исключение которое создали чтобы его вызывали

"=============================Вызов исключений============================"

# raise NameError("666666666666666666ERRORERRORERRORERROR")

"=============================Обработка исключений=========================="

# Чтоббы код не прекращал работу, мы можем использовать конструкцию try except,  и обрабатывать вызваные исключения

# try:
#     # код который возможно выведет ошибку
#     num = int(input('Введите число:'))
# except ValueError: # ошибка, которая может возникнуть
#     print('вы ввели не число!')
# else:
#     # код, который отработает, только если ошибка не вышла
#     print(num)
# finally:
#     # Код, который отрабатывает в любом случае
#     print('до свидания!')

# try:
#     raise ValueError('Error')
# except (SyntaxError, NameError):
#     print('Вышла одна из указанных ошибок')

# try:
#     raise TypeError('Type Error')
# except Exception as e:
#     print(e)

#1

# try:
#     ...
# except:
#     ...
# else:
#     ...
# finally:
#     ...
# #2
# try:
#      a = 6
#      print (a)
# except NameError:
#      print("Такой переменной не существует!")

# #3
# try:
#     a = int(input('Введите первоечисло:'))
#     b = int(input('Введите второе число:'))
#     print(a/b)
# except ZeroDivisionError:
#     print( "На ноль делить нельзя")
# #4
# try:
#     c = float(input('Введите дробное число:'))
#     d = float(input('Введите второе дробное число:'))
#     print(round(c) + round(d))
# except ValueError:
#     print('Введите число!')
# #5
# try:
#     dict1 = {a:'1', b:'2', c:'3'}
#     u = (dict1.keys())
#     print(u)
# except KeyError:
#     print('Такого ключа нет')
# #6
# try:
#     l = (1, 2, 3, 4, 5, 6, 7)
#     print(l[1000])
# except IndexError:
#     print('Нет такого элемента')
# #7
# try:
#     m = int(input('Введите свой возраст:'))
#     if m < 18:
#         raise ValueError
# except ValueError:
#     print('Доступ запрещен')
# else:
#     print('Введен неккоректный возраст')
# finally:
#     print('Спасибо, До свидания!')


# try:
#     g1 = int(input('Введите первое число'))
#     g2 = int(input('Введите второе число'))
#     print(g1/g2)
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка')

# try:
#     j = float(input("Введите сумму денег:"))
#     if j < 0:
#         raise ValueError('Сумма не может быть отрицательной')
# except ValueError:
#     print('Введите корректное число')
# else:
#     print(j)

# try:
#     a = input('Введите строку:')
#     b = int(input('Введите число:'))
#     print(a+b)
# except TypeError:
#     print('Unsupported option')


# try:
#     list1.extend('list2')
# except NameError:
#     print('list does not exist')

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# try:
#     for i in range(0, len(list1) + 1):
#         print(list1[i])
# except IndexError:
#     print('Error')


warehouse = [
    [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
    ['1', '2', '3'],
    [1, 2, 3, 4 , 5, 6],
    [[1], [2], [3]],
    [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
]

# a = len(warehouse)
# if a > 10:
#     raise ValueError


# for i in warehouse:
#     if len(i) > 3:
#         raise ValueError
    
# a = 10
# try:
#     while a < 1000000000000000000000:
#         print(a)
#         a = a - 1
# except KeyboardInterrupt:
#     print('Nope')

list1 = []
a = input().split() 
for i in a:
    try:
        list1.append(int(i))
    except ValueError:
        print("Данный элемент не является числом!")
print(list1)






