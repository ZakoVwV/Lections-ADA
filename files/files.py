# "======================================Модули и пакеты===================================="
# # любой файл с расширением .py - модуль

# # пакет - набор модулей (обязательно должен быть файл __init__.py)
# "======================================Работа с файлами===================================="
# # open - функция которая открывает файл в определенном режиме
# "режимы"
# """
# r - read(открываем файл только для чтения, методы для записи работать не будут)
# w - write (открываем файл только для записи, при каждом запуске файла очищается и записывается новые данные)
# a - append (открываем файл для дозаписи, новые данные записываются в конец и не стираются как случае с режимом "w")
# x - Создает новый файл, но если такой файл уже существует то выйдет ошибка)
# b - binary (файл в бинарном виде)
# """
# "========================================Read======================================="
# file = open ('files/test.txt', 'r')
# # print(file) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# # print(dir(file))
# # writable - метод, который возвращает True если в файл можно что-то записать, и False - если файл только для чтения
# # print(file.writable()) # False

# # readable() - метод который также возвращает булевые значения (True/False), но проверяет, можно ли считать файл

# # print(file.readable()) # True
# # read() - метод который считывает весь файл (если режим выбран "w", то этот метод будет недоступен)
# print(file.read())
# print(file.read()) # ' ' - возвращает пустоту, потому что каретка находится в конце
# # метод сик переносит каретку на указанную позицию, 0 - самое начало
# # file.seek(0)
# print(file.read(5)) # hello
# file.seek(0)
# # print(file.read(7))

# #readlines() - метод, который считывает весь файл и возвращает список со строками
# print(file.readlines()) # ['hello\n', 'ada\n', 'courses\n', '\n', '\n']

# #readline() - считывает одну строку и возвращает тир данных str

# file.seek(0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# # close() - метод который позволяет закрыть файл, и сделать его недоступным для работы, если не закрыть вручную через close(), то файл будет постоянно открыт
# file.close()
# "======================================Write========================================="
# # file.read() ValueError: I/O operation on closed file.
# """
# в режиме w указанного файла не существует, то он создается автоматически, если же файл существует, то он стирает все, и записывает новые данные

# write() - метод который принимает строку и возвращает её

# writelines() - метод, который принимает список из строк, и записывает в файл
# """
# file2 = open('files/test2.txt', 'w')
# file2.write('hello\n')
# file2.write('world\n')

# file2.writelines(['my\n', 'name\n', 'is\n', 'Amir'])

# file2.close()
# "==========================================append==========================================="
# file3 = open('files/test3.txt', 'a')
# print(file3.readable()) # False
# file3.write('Lections ADA')

# file3.writelines(['Amir\n'])
# file3.close()
# "=====================================Контекстный менеджер==============================="
# # конструция with ... as ...

# # with open('test3.txt', 'r') as file4:
# #     print(file4.read())

"===================================CSV========================================"
# csv - (Comma Separated Values)
"""
Текстовый формат, который используется для хранения данных в виде таблицы

Для работы с CSV файлами вам нужен модуль CSV
import csv
"""

# csv.writer() - Создает объект для записи в CSV файл
# csv.reader() - Создает объект для чтения из CSV файла

"===================================Методы для записи в CSV файл============================="
# writer.writerow() - это запись одной строки в CSV файл


import csv

with open ('files/test.csv', 'w') as scvfile:
    writer = csv.writer(scvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Amir', '14', 'Bishkek'])

# writer.writerows() - Запись нескольких строк сразу
data = [
    ['Marka', 'god izdania', 'cena'],
    ['Ford mustang', 2017, 21000],
    ['Mercedes 220', 2007, 1000],
    ['BMW m8', 2024, 150000]
]
with open ('files/writerows.csv', 'w') as file:
    writer = csv.writer(file) 
    writer.writerows(data)


with open ('files/writerows.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# csv.DictWriter - создание объектов для записи данных в виде словаря

with open ('files/example.csv', 'w') as file:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader() # Записывает заголовок
    writer.writerow({'name':' Alice', 'age': '22', 'city':'New yourk'}) 
