"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


n = 345937
print(timeit.timeit('revers(n)', setup='from __main__ import revers, n'))
print(timeit.timeit('revers_2(n)', setup='from __main__ import revers_2, n'))
print(timeit.timeit('revers_3(n)', setup='from __main__ import revers_3, n'))

cProfile.run('revers(n)')
cProfile.run('revers_2(n)')
cProfile.run('revers_3(n)')

"""
Последний алгоритм является самым эффективным, потому что использует встроенные функции Python (срезы [::-1]), которые
"заточены" под скорость.
1 и 2 алгоритмы делают одно и тоже, но второй алгоритм быстрее первого, так как в нём используется цикл, 
а в первом используется рекурсия.
"""

