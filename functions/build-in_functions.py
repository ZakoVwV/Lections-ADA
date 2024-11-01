"==============================Встроенные функций==============================="
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько псоледовательностей (получаем генератор, в котором элементы это - tuple)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [10.1, 10.2, 20.6]

zipped = zip(list1, list2, list3)
print(zipped) # <zip object at 0x000002A98DFAF880>

zipped = list(zip(list1, list2, list3))
print(zipped) # [(1, 'a', 10.1), (2, 'b', 10.2), (3, 'c', 20.6)]

for element in zipped:
    print(element)

# (1, 'a', 10.1)
# (2, 'b', 10.2)
# (3, 'c', 20.6)

list4 = [1, 2, 3, 4, 5]
list5 = ['a', 'b', 'c', 'd', 'e']
dict_ = dict(zip(list4, list5))
print(dict_)
"===========================Enumerate=============================="
# enumerate - нумерует последовательности (по дефолту начинает с 0) (так - же как с zip() получаем генератор)

enumerated = enumerate('hello')
print(enumerated)

for element in enumerated:
    print(element)

string = 'hello world'
print(list(enumerate(string)))
"=============================map================================="
# map - это функция которая принимает в аргументы функцию и последовательность, и применяет эту функцию к элементу последовательности(записывает в новую последовательность результат функций, в которую передаются элементы последоватлеьности)

# поменяйте тип данных жлементов list_ со строк на числа
list_ = ['1', '2', '3', '4', '5']
mapped_list = list(map(int, list1))
print(mapped_list)

# создать новый список элемеентый которого квадраты элементов list1
list1 = [12, 13, 14, 15, 16, 17]
# mapped_list = list(map(lambda x: x**2, list1))
# print(mapped_list)

def to_2_degree(x):
    return x**2

mapped_list = list(map(to_2_degree, list1))
print(mapped_list)

a = [i ** 2 for i  in list1]

print(a)

'==============================Filter================================'
# filter - возвращает генератор с элементами, прошедшая фильтр (какое то условие), принимает в себя: 1) функцию 2) последовательность

list1 = [1, 0, -1, -23, -55, 13, 22]
# отфильтрировать элементы списка, оставить только те, которые больше 0
filtered = list(filter(lambda x: x > 0, list1))
print(filtered)

list_ = list(range(1, 51))
# Отфильтровать list_, оставить только четные числа
filtered = list(filter(lambda x: x%2 == 0, list_))
print(filtered)

users = [
    {'name':'Nikita', 'age':10},
    {'name': 'nasrya', 'age': 34},
    {'name': 'tima', 'age': 19}
]
# отфильтровать пользователей, оставить только тех, кому больше 18

solution = [i for i in users if i['age'] > 18]
print(solution)

solution2 = list(filter(lambda user: user['age'] > 18, users))
print(solution2)
"=================================reduce===================================="
from functools import reduce
# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна обязательна принимать 2 аргумента)

list1 = list(range(1, 101))
result = reduce(lambda x, y: x + y, list1)
print(result) # 5050


string = 'hello'
res = reduce(lambda x, y: x + '%' + y, string)
print(res)

list6 = ['hello','gummy','funnier', 'hello world']
comp = list(filter(lambda x: len(x)>7, list6))
print(comp)

list7 = [2, 5, 3, 7, 9, 15, 4]
chet = len(list(filter(lambda x: x%2 == 0, list7)))
nechet = len(list(filter(lambda x: x%2 != 0, list7)))
print(f'четные: {chet}')
print(f'нечетные: {nechet}')

list8 = ['hello','gummy','funnier', 'hello world']
highest = reduce(lambda x, y: x if len(x) > len(y) else y, list8)
print(highest)


list9 = [*range(1, 51)]
result1 = list(map(lambda x:'fizz' if x %3 ==0 else 'buzz', list9))
print(result1)

list0 = [*range(1, 51)]
result0 = reduce(lambda x, y: x if x < y else x, list0)
print(result0)

