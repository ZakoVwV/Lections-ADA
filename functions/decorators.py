"================================Декораторы============================="
# Функция вышего порядка - это функция которая принимает в аргументы другую функция, затем создает внутри себя функцию, вызывает функцию, возвращает функцию

# Декоратор - это функция высшего порядка которая нужна чтобы расширять функционал функций не изменяя её функционал (функция обертка)

# как пишутся декораторы

def time_decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print(f'start: {datetime.now()}')
        func(*args, **kwargs)
        print(f'finish: {datetime.now()}')
    return wrapper

@time_decorator
def hello():
    print('hello')

# hello()

def func_total_time(func):
    def wrapper(*a, **k):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime('%d.%m.%Y. %H:%M')
        print(f'Функция запущена {correct_format}')
        func(*a, **k)
    return wrapper

@func_total_time
def iterate_list(list_):
    for i in list_:
        print(i)

# iterate_list([1,1,1,1,1,1,1,1])


# def iter_decorator(num: int):
#     def inner_decorator(func):
#         def wrapper(*a, **k):
#             for i in range(num):
#                 func(*a, **k)
#         return wrapper
#     return inner_decorator

# @iter_decorator(100)
# def hello():
#     print('hello')

# hello()
from time import time


def benchmark(func):
    def wrapper(*a, **k):
        start = time()
        func(*a, **k)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функций: {total_time} секунд')
    return wrapper

@benchmark
def iter_range():
    count = 0
    for i in range(1, 1000001):
        count += i
    print(count)
iter_range()




