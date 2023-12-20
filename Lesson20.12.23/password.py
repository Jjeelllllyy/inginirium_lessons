def ask_password():
    password = input('Введите пароль:')
    if password == 'пароль':
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')


ask_password()

