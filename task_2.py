"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

from hashlib import sha256
salt = 'impossible_password'


def create_hash(pwd):
    global salt
    return sha256(pwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def authorization(pwd):
    global salt
    with open('data.txt', 'r') as read_file:
        return True if sha256(pwd.encode('utf-8') + salt.encode('utf-8')).hexdigest() == read_file.read() else False


password_hash = create_hash(input('Введите пароль: '))
print('В файле хранится строка:', password_hash)

with open('data.txt', 'w') as write_file:
    write_file.write(password_hash)

del password_hash

password = input('Введите пароль еще раз для проверки: ')
print(f'Вы ввели {"" if authorization(password) else "не"}правильный пароль')
