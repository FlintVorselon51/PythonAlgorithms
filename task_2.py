"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import defaultdict

"""
В Python уже есть реализация шестнадцатеричных чисел:
a = int('0xA2', 16)
b = int('0xC4F', 16)
print(hex(a+b), hex(a*b))
"""

a = list(input('Enter First Number: '))
b = list(input('Enter Second Number: '))
d = defaultdict(int)
d[a] = int('0x' + ''.join(a), 16)
d[b] = int('0x' + ''.join(b), 16)
print(list(hex(sum(d.values()))[2:].upper()))
mul_res = int('1', 16)
for el in d.values():
    mul_res *= el
print(list(hex(mul_res)[2:].upper()))

"""ООП"""


class HexNumber:
    def __init__(self, value):
        self.value = int('0x' + ''.join(value), 16)

    def __add__(self, other):
        return HexNumber(list(hex(self.value + other.value))[2:])

    def __mul__(self, other):
        return HexNumber(list(hex(self.value + other.value))[2:])

    def __str__(self):
        return str(list(hex(self.value)[2:].upper()))


a = HexNumber(['A', '2'])
b = HexNumber(['C', '4', 'F'])
print(a + b)
print(a * b)
