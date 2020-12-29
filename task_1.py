"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    # Использование генераторного выражения снижает время выполнения минимум в 1.5 раза
    return [el for el in nums if el % 2 == 0]


lst = list(range(10))
print(timeit.timeit('func_1(lst)', setup='from __main__ import func_1, lst'))
print(timeit.timeit('func_2(lst)', setup='from __main__ import func_2, lst'))
