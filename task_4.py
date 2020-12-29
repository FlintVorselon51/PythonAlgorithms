"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    # r - число, m - сколько раз оно встречается
    m = r = 0
    for el in set(array):
        tmp = array.count(el)
        if tmp > m:
            m = tmp
            r = el
    return r, m


print(timeit.timeit('func_1()', setup='from __main__ import func_1'))
print(timeit.timeit('func_2()', setup='from __main__ import func_2'))
print(timeit.timeit('func_3()', setup='from __main__ import func_3'))

"""Я использвал преобразование списка в множество, для чтобы уменьшить количетво вызовов метода count"""
