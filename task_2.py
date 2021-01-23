"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

from memory_profiler import profile
from recordclass import recordclass, make_dataclass
from collections import namedtuple

"""
Использование recordclass и make_dataclass из библиотеки recordclass позволяет уменьшить используемую память.
recordclass похоже на namedtuple, использует меньше памяти и поддерживает изменение значения объектов (т.е. можно
связать объект-значение ob.x с другим объектом-значением. Если эта функциональность нам не нужна, то можно использовать
make_dataclass, который использует еще меньше памяти.

namedtuple      8.6 MiB
recordclass     7.5 MiB
make_dataclass  5.8 MiB

--- recordclass ---
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     19.0 MiB     19.0 MiB           1   @profile
    17                                         def f(name_of_class, n):
    18     26.5 MiB      7.5 MiB      100003       res = [name_of_class(1, 2, 3) for _ in range(n)]
    19     26.5 MiB      0.0 MiB           1       return res

--- make_dataclass ---
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     19.2 MiB     19.2 MiB           1   @profile
    17                                         def f(name_of_class, n):
    18     25.0 MiB      5.8 MiB      100003       res = [name_of_class(1, 2, 3) for _ in range(n)]
    19     25.0 MiB      0.0 MiB           1       return res

--- namedtuple ---
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     19.4 MiB     19.4 MiB           1   @profile
    17                                         def f(name_of_class, n):
    18     28.1 MiB      8.6 MiB      100003       res = [name_of_class(1, 2, 3) for _ in range(n)]
    19     28.1 MiB      0.0 MiB           1       return res 
"""

Point1 = recordclass('Point1', ('x', 'y', 'z'))
Point2 = make_dataclass('Point1', ('x', 'y', 'z'))
Point3 = namedtuple('Point2', ('x', 'y', 'z'))

a = Point3(1, 2, 3)


@profile
def f(name_of_class, n):
    res = [name_of_class(1, 2, 3) for _ in range(n)]
    return res


f(Point1, 10**5)
f(Point2, 10**5)
f(Point3, 10**5)
