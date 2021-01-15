"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

import timeit
from collections import deque

lst = list()
dq = deque()

print('Вставка в конец списка')
print(timeit.timeit('lst.append(0)', setup='from __main__ import lst', number=10**6))

# Всего 1000 раз, т.к. операция вставки в начало списка очень медленная. Вообще списки не реккомендуется использовать,
# если требуется вставлять данные в начало. Время её выполнения зависит от того, сколько уже элементов в списке.
print('\nВставка в начало списка')
print(timeit.timeit('lst.insert(0, 1)', setup='from __main__ import lst', number=1000))

print('\nВставка в конец двусторонней очереди')
print(timeit.timeit('dq.append(0)', setup='from __main__ import dq', number=10**6))

print('\nВставка в начало двусторонней очереди')
print(timeit.timeit('dq.appendleft(1)', setup='from __main__ import dq', number=1000))

print('\n"Вытаскивание" из конца списка')
print(timeit.timeit('lst.pop()', setup='from __main__ import lst'))

lst.pop()
lst = [0 for _ in range(10**6)]

print('\n"Вытаскивание" из начала списка"')
print(timeit.timeit('lst.pop(0)', setup='from __main__ import lst', number=1000))

print('\n"Вытаскивание" из конца двусторонней очереди')
print(timeit.timeit('dq.pop()', setup='from __main__ import dq'))

dq.pop()
dq = deque([0 for _ in range(10**6)])

print('\n"Вытаскивание" начала двусторонней очереди')
print(timeit.timeit('dq.popleft()', setup='from __main__ import dq', number=1000))

print('\nСлучайный доступ к элементам списка')
print(timeit.timeit('lst[randint(0, 10**5)]', setup='''
from __main__ import lst
from random import randint'''))

print('\nСлучайный доступ к элементам двусторонней очереди')
print(timeit.timeit('dq[randint(0, 10**5)]', setup='''
from __main__ import dq
from random import randint'''))

"""
Сделав замеры, убедимся, что информация в документации соответствует действительности.

Операции, связанные с "концом" структуры данных (вставка в конец или удаление из конца),
и в списоке и двусторонней очереди выполняются примерно за равное время, однако двусторонняя очередь всё же быстрее.

Операции, связанные с "началом" структуры данных (вставка в начало или удаление из начала) опреденно выполняются
гораздо быстрее (в тысячи раз) в двусторонней очереди, нежели в списках. 
Время выполнения таких операций в списке очень сильно зависит от длины самого списка, потому что когда мы
хотим что-то вставить в начало или конец списка, то приходится грубо говоря полностью "пересобирать" список.

Двусторонняя очередь проигрывает списку по скорости в несколько раз, при операциях доступа к элементам.
"""
