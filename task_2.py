"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def roll_str(s):
    if len(s) == 1:
        return s
    return roll_str(s[1:]) + s[0]


n = 4963414784
print('--- Без мемоизации ---')
print(timeit.timeit('recursive_reverse(n)', setup='from __main__ import recursive_reverse, n'))

print('--- С мемоизацией ---')
print(timeit.timeit('recursive_reverse_memo(n)', setup='from __main__ import recursive_reverse_memo, n'))

print('--- Сторонняя функция с рекурсией ---')
print(timeit.timeit('roll_str(str(n))', setup='from __main__ import roll_str, n'))

"""
Используем декоратор для мемоизации.
Как видим мемоизация сильно уменьшает время выполнения, если в функцию поступают значения, которые уже поступали ранее.
"""
