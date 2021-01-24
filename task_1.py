"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random

"""
Доработав сортировку пузырьком, заметим, что сортировка в большинстве случаев немного замедляется, но бывает, что
она немного быстрее чем без доработки. Всё, конечно, зависит от входного массива
"""


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def smart_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        cnt = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                cnt += 1
        if cnt == 0:
            break
        n += 1
    return lst_obj


lst = [4, 3, 6, 2, 5, 9, 7, 1, 8]
print(lst)
print(bubble_sort(lst.copy()))
print(smart_bubble_sort(lst.copy()))


orig_list = [random.randint(-100, 100) for _ in range(400)]

# замеры 1000
print(timeit.timeit(
    "bubble_sort(orig_list.copy())", setup="from __main__ import bubble_sort, orig_list", number=10))
print(timeit.timeit(
    "smart_bubble_sort(orig_list.copy())", setup="from __main__ import smart_bubble_sort, orig_list", number=10))
