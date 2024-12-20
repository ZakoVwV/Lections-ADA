"============================Типы данных============================="
# 1) изменяемые (dict, set, list)
# 2) неизменяемые (tuple, int, string, float, bool, None, frozenset)

"=============================Numbers================================="
# числа - неизменяемый тип данных, неитерируемый тип данных для хранения чисел и проведения над ними арифметических действий

int # целые числа
float # вещественные, дробные, десятичные, с плавающей точкой
# decimal # десятичные но более точные

"================================String=================================="
# строка - неизменяемый, итерируемый, индексируемый тип данных преддназначеннный для хранения строк, последовательность символов, заключенных в кавычки

str1 = 'hello'
str2 = "hello"
str3 = """hello"""
str4 = '''hello'''
# error = 'hello"
"================================Индексы==================================="
# строка - нумерация каждого элемента, которая начинается с 0
string = 'hello world'
print(string[-1])
print(string[5])

"================================Срезы===================================="
# срезы - часть последовательности (в случае со строками, срез дает нам подстроку) (начало:конец:шаг)

string = 'some string'
print(string[0:4])
print(string[:4])
"================================List==================================="
# список - изменяемый, итерируемый, индексируемый тип данных для хранения последовательности элементов(может содержать любые данные)
list1 = [1, 'str', None, False, True, [1], {1: 1}, 1.1]

list1[-1]

"================================Tuple=================================="
# tuple - неизменяемый. индексируемый, итерируемый тип данных, литералы - запятые. По сути просто неизменяемый список
num = (1) # int
tuple = (1,) # tuple
tuple2 = 1,2,3,4,5,5 # tuple
"================================Set===================================="
# set - изменяемый, индексируемый, итерируемый тип данных для хранения уникальных, литералы - {}
set1 = {} # dict
set1 = set() # set
set2 = {1, 1, 1, 2, 2, 3, 4, 5, 6, 6} # {1, 2, 3, 4, 5, 6}
set3 = {1, 0, True, False} # {1, 0}
set4 = {True, 0, False, 1} # {True, 0}
# remove() - удаляет элемент

"==============================frozen set============================"
# set - неизменяемый set, все методы которые были у set, во frozenset отсутсвуют
f_set = frozenset([1, 2, 3, 4, 1, 1]) # {1, 2, 3, 4}

"===============================Dict================================="
# dict - изменяемый, итерируемый, неиндексируемый тип данных для хранений пар ключ:значение
# ключи - ключи должны быть только неизменяемые ключи данных
# если ключом будет кортеж, то в нем тоже должны быть только неизменяемые типы данных
# если ключ повторяется - значение перезаписывается на последнее

dict1 = {'a':1, 'b': 2, 'a': 3} # {'a': 3, 'b': 2}
print(dict1)

"=================================Bool================================="
# bool - логичесский тип данных, с двумя значениями (True, False/ 1, 0)

"==================================NoneType==============================="
# None - это тип данных для обозначения отсутсвия знасения

"=================================Conditions=============================="
# условие - конструкция которая при разных условиях позыволяет выполнять или не выполнять какой то кусок кода, которая находится в теле условия

# if условие1:
#     ...
# elif условие2:
#     ...
# else:
#     ...
"=============================Тернарные операторы========================="
# тернарные операторы - условие if else в одну строчку
# 'res1' if условие else res2

"===============================циклы=================================="
# цикл - блок кода, который будет выполняться несколько раз.

# итерация - это 1 круг цикла

# итератор - for

# итерируемый объект - объект по которому мы проходимся циклом

# continue - пропускает 1 итерацию (шаг)

# break - полностью останавливает работу цикла
"================================For==================================="
# for - цикл, который проходится по элементам итерируемого объекта (str, list, dict, tuple, range). В цикле for мы выполняем какие то операций над элементами объекта, останавливается когда доходит до последнего элемента в последовательности

list1 = [1,2,3,4,5]
for i in list1:
    print(i)


"===================================while===================================="
# while - цикл, который работает до тех пор пока условие которое ему было задано верно (True) (может быть бесконечным)
# num = 10

# while num:
#     print(num)
