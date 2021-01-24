"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import random
from statistics import median


def select_median(lst):
    return select(lst, len(lst) / 2)


def select(lst, k):

    if len(lst) == 1:
        return lst[0]

    # Опорный элемент
    pivot = random.choice(lst)

    lows = [el for el in lst if el < pivot]
    highs = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(lows):
        return select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return select(highs, k - len(lows) - len(pivots))


# Проверка работы программы
arr = [random.randint(-10000, 10000) for _ in range(999)]
print(select_median(arr))
print(median(arr))
