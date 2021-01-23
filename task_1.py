"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import numpy as np
from memory_profiler import profile

"""
Python 3.8.6 x64
"""

"""
1. Использование numpy массивов значительно уменьшает объем используемой памяти
Задача: получить целые числа от 0 до N.
Функция, использующая numpy использует приблизительно в 10 раз меньше памяти, чем функция, возвращающяя список.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     29.9 MiB     29.9 MiB           1   @profile()
    40                                         def f1(n):
    41     33.7 MiB      3.8 MiB           1       res = list(range(n))
    42     33.7 MiB      0.0 MiB           1       return res

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    59     30.3 MiB     30.3 MiB           1   @profile()
    60                                         def f2(n):
    61     30.6 MiB      0.4 MiB           1       res = np.arange(0, n)
    62     30.6 MiB      0.0 MiB           1       return res

"""


@profile()
def f1(n):
    res = list(range(n))
    return res


@profile()
def f2(n):
    res = np.arange(0, n)
    return res


f1(10**5)
f2(10**5)


"""
__slots__ на примере из курса основ (урок 6 задание 2)
Необходимо реализовать класс дороги (Road), в котором определить два атрибута (length и width).
Использование __slots__ может уменьшить используемую память в несколько раз:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    89     31.2 MiB     31.2 MiB           1   @profile
    90                                         def create_road(n):
    91     33.9 MiB      2.8 MiB       40003       return tuple(Road(1, 1) for _ in range(n))

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    94     31.4 MiB     31.4 MiB           1   @profile
    95                                         def create_road_slots(n):
    96     31.8 MiB      0.3 MiB       40003       return tuple(RoadSlots(1, 1) for _ in range(n))
"""


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width / 8


class RoadSlots:
    __slots__ = ('length', 'width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width / 8


@profile
def create_road(n):
    return tuple(Road(1, 1) for _ in range(n))


@profile
def create_road_slots(n):
    return tuple(RoadSlots(1, 1) for _ in range(n))


create_road(10**4 * 2)
create_road_slots(10**4 * 2)

"""
Количество используемой памяти также зависит от способа как вы решаете задачу.
Например, имеется двумерный массив размером n x 2:
34 243
32 212
234 21
400 1
Требуется найти максимальную сумму двух чисел, которые являются парой. (т.е. в данном примере это 401)
Мы можем искать сумму каждой пары и проверять не больше ли она максимальной (классический способ нахождения
максимального элемента) или создать список сумм и найти в нем максимальное значение. Второй способ выглядит 
легче и лаконичнее, однако использует много памяти, по сравнению с первым способом, в котором память практически
не выделяется.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   126     30.6 MiB     30.6 MiB           1   @profile
   127                                         def find_pair1(arr):
   128     30.6 MiB      0.0 MiB           1       res = None
   129     30.6 MiB      0.0 MiB      100001       for pair in arr:
   130     30.6 MiB      0.0 MiB      100000           s = sum(pair)
   131     30.6 MiB      0.0 MiB      100000           if res is None or s > res:
   132     30.6 MiB      0.0 MiB           8               res = s
   133     30.6 MiB      0.0 MiB           1       return res

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   136     30.6 MiB     30.6 MiB           1   @profile
   137                                         def find_pair2(arr):
   138     34.7 MiB      4.1 MiB      100003       pair_sums = [sum(pair) for pair in arr]
   139     34.7 MiB      0.0 MiB           1       return max(pair_sums)
   
"""


@profile
def find_pair1(arr):
    res = None
    for pair in arr:
        s = sum(pair)
        if res is None or s > res:
            res = s
    return res


@profile
def find_pair2(arr):
    pair_sums = [sum(pair) for pair in arr]
    return max(pair_sums)


test_arr = np.random.randint(0, 10**4, (10**5, 2), dtype=np.int16)
find_pair1(test_arr)
find_pair2(test_arr)
