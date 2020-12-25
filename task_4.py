"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

"""
Решение 1
Хранилище оформляем в виде списка кортежей
Итоговая сложность: O(n) из-за перебора списка
"""

# Данные в виде списка кортежей (логин, пароль, активирована (True) / неактирована (False))
data = [
    ('oleg1990', '12345678', True),
    ('liza666', 'strong_password', False),
    ('anton2011', 'really_strong_password', True),
    ('ivan_ivanov', 'qwerty', False)
]


def authorization1(dataset, login, password):
    for combination in data:
        if combination[0] == login:
            return True if combination[1] == password and combination[2] is True else False
    return False


authorization1(data, 'oleg1990', '12345678')  # --> True
authorization1(data, 'oleg1990', '12345677')  # --> False
authorization1(data, 'liza666', 'strong_password')  # --> False
authorization1(data, 'unknown_login', 'abc')  # --> False

"""
Решение 2
В качестве хранилища используем словарь, где ключом является логин
Итоговая сложность: O(1)
"""

data = {
    'oleg1990': ('12345678', True),
    'liza666': ('strong_password', False),
    'anton2011': ('really_strong_password', True),
    'ivan_ivanov': ('qwerty', False)
}


def authorization2(dataset, login, password):
    try:
        return dataset[login][0] == password and dataset[login][1] is True
    except KeyError:
        return False


authorization2(data, 'anton2011', 'really_strong_password')  # --> True
authorization2(data, 'anton2010', 'really_strong_password')  # --> False
authorization2(data, 'ivan_ivanov', 'qwerty')  # --> False

"""
Вывод
Решение 2 эффективнее первого, поскольку имеет константное время работы, благодаря словарям.
"""
