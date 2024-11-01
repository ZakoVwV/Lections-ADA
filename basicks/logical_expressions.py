"==================================Логические и условные операторы============================="
# логические операторы - это выражения, которые возвращают True, если выражение верное, False - если не верное

"равенство"
5 == 5 # True
5 == 10 # False

"Не равенство"
4 != 5 # True
4 != 4 # False

"больше"
4 > 5 # False
4 > 3 # True

"меньше"
4 < 10 # True
4 < 1 # False

"меньше или равно"
4 <= 4 # True
4 <= 1 # False

"больше или равно"
4 >= 10 # False
4 >= 4 # True


'5' == 5 # False
'hello' == 'hello' # True
'Hello' == 'hello' # False

"======================================and/or/not=============================================="
# and - и 
# or - или
# not - не

a = 5
b = 6

# False      True
a == 1 and b == 6 # False
# если все части выражения возвращают True - будет True
# если будет возвращен хоть 1 False - в конечном итоге будет False

# False    True
a == 1 or b == 6 # True
# Если хотя бы одна часть вернет True - будет True


not True # False
not False # True
not not True # True

not a == 5 # False(потому что а равна 5)
not a == 4 # True (потому что а не равна 4)

"========================================Boolean Type================================="

bool(1) # True
bool(0) # False
bool(-122) # True

print(bool('hello')) # True
print(bool(' ')) # True
print(bool('')) # False

print(bool(True)) # True
print(bool(False)) # False


print(bool([])) # False
print(bool([[]])) # True

"===========================================None Type==================================="
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения

print(bool(None)) # False
print(bool('None')) # True

a = None
print(a is None) # True(is это проверка на полное соответствие, включая тип данных)

"===============================Условные операторы========================"
# Условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному(в зависимости от условия)

# if условие1:
#     тело1
    # тело1 будет выполняться только если условие1 верное

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное
# else:
#     тело2 
#     # тело2 будет выполняться во всех других случаях (в данном примере, else выполнится если условие1 вернет False)

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное
# elif условие2:
#     тело2
#     # тело2 будет выполняться только если условие1 не верное, а условие2 верное

# if условие1:
#     тело1
#     # тело1 будет работать, если условие1 верное
# elif условие2:
#     тело2
#     # тело2 будет работать, если условие 1 не верное, а условие2 верное
# else:
#     тело3
#     # тело3 будет выполняться только если все вышеуказанные условие не верные

"""
1. в одной конструкции мы можем только 1 if
2. в одной конструкции мы можем использовать сколько угодно elif
3. в одной конструкции мы можем использовать только 1 else или не использовать вообще
"""

"""
Запросить у пользователя число, и проверить, является ли это число положительным, либо отрицательным, либо - 0, вывести соответствующее сообщение
"""

# num = int(input('Введите число: '))
# if num == 0:
#     print(f'число {num} - это ноль')
# elif num > 0:
#     print(f'число {num} - положительное')
# else:
#     print(f'число {num} - отрицательное')


"==============================Тернарные операторы=============================="
# тернарные операторы - условия в одну строку
# тело1 if условие else тело2
# тернарный оператор нельзя написать с if, но без else
# в тернарый оператор нельзя добавить elif, и еще одну проверку


"""
примите от пользователя число и выведите строку 'hello' если число == 5, в ином случае верните 'bye'
"""

# num1 = int(input())
# result = 'hello' if num1 == 5 else 'Bye'
# print(result)

"=================================FizzBuzz==============================="
"""
примите число от пользователя
выведите Fizz, если кратно 3
выведите Buzz, если число кратно 5
выведите FizzBuzz, если число кратно и 3 и 5
выведите число во всех остальных случаях
"""

# 1 способ
# num = int(input('Введите число: '))

# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)


# 2 способ
num = int(input())
if num % 15 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)
