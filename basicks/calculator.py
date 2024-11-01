
while True:
        try:
            a = int(input('Введите 1 число: '))
            b = int(input('Введите 2 число: '))
            print('Выберите +, -, *, /, %, **, //')
            c = input()
            if c == '+':
                print(a + b)
            elif c == '-':
                print(a - b)
            elif c == '*':
                print(a * b)
            elif c == '/':
                print(a / b)
            elif c == '%':
                print(a % b)
            elif c == '**':
                print(a ** b)
            elif c == '//':
             print(a // b)
            else:
                print('Данной операций нет в системе')
        except:
                print('Вы неправильно ввели значение')
        print("Хотите продолжить(yes/no)?")
        d = input()  
        if d != 'yes':
            print('До свидания')
            break
