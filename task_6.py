"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint


def guess(n=0, cnt=0):
    if cnt == 0:
        n = randint(0, 100)
    if cnt == 10:
        print('Вы не угадали число за 10 попыток')
        return
    try:
        s = int(input('Попробуйте угадать целое число от 0 до 100: '))
        if s == n:
            print('Вы угадали!')
        print('Вы не угадали, загаданное число', 'больше' if n > s else 'меньше')
        return guess(n, cnt + 1)
    except ValueError:
        print('Вы ввели строку, которую невозможно преобразовать к числу')
        return guess(n, cnt)


guess()
