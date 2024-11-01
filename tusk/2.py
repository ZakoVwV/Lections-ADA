with open ('tusk/users.txt', 'w') as file:
    print('Введите логин и пароль:')
    log = input('Login:')
    pasw = (input('Pasword:'))
    print('Вы успешно зарегистрировались')
    file.writelines([log, ' ', pasw])

