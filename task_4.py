"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit
from collections import OrderedDict


def remove_for_dict(dictionary):
    dictionary[0] = 0
    del dictionary[0]


d = dict()
od = OrderedDict()

print(timeit.timeit('d[0] = 0', setup='from __main__ import d', number=10**7))
print(timeit.timeit('od[0] = 0', setup='from __main__ import od', number=10**7))

print(timeit.timeit('d[0]', setup='from __main__ import d', number=10**7))
print(timeit.timeit('od[0]', setup='from __main__ import od', number=10**7))

print(timeit.timeit('remove_for_dict(d)', setup='from __main__ import d, remove_for_dict'))
print(timeit.timeit('remove_for_dict(od)', setup='from __main__ import od, remove_for_dict'))

"""
В среднем, OrderedDict незначительно медленнее обычного словаря.
Нет нужны в OrderedDict, если версия интерпретатора 3.6 или выше
"""
