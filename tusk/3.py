with open ('tusk/3.txt', 'r') as file:
    if 'w' in file.read():
        print('Да, в тексте содержтся буква w')
    else:
        print('Нет, в тексте не содержтся буква w')
