"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

"""Задания перепутаны!?"""


class PlateStack:
    """Класс структуры стопок тарелок"""

    def __init__(self, limit):
        self.limit = limit
        self.__stacks = []

    def add(self, number_of_plates=1):
        """Добавляет тарелки в структуру"""
        for i in range(number_of_plates):
            if len(self.__stacks) == 0 or len(self.__stacks[-1]) == self.limit:
                self.__stacks.append(Stack())
            self.__stacks[-1].add('Тарелка')

    def remove(self, number_of_plates=1):
        """Убирает тарелки из структуры"""
        for i in range(number_of_plates):
            if len(self.__stacks) == 0:
                return
            self.__stacks[-1].pop()
            if len(self.__stacks[-1]) == 0:
                self.__stacks.pop()

    def __str__(self):
        s = ' '.join([str(len(stack)) for stack in self.__stacks])
        return 'Количество стопок: ' + str(len(self.__stacks)) + '\nСостояние стопок: ' + s + '\n'


class Stack:
    def __init__(self):
        self.__lst = []

    def add(self, element):
        """Добавляет элемент в стек"""
        self.__lst.append(element)

    def pop(self):
        """Удаляет последний элемент из стека"""
        return self.__lst.pop()

    def __len__(self):
        """Возвращает длину стека"""
        return len(self.__lst)


plate_stack = PlateStack(2)

print(plate_stack)

plate_stack.add(2)
print(plate_stack)

plate_stack.add(7)
print(plate_stack)

plate_stack.remove()
print(plate_stack)

plate_stack.remove(7)
print(plate_stack)

plate_stack.remove(100)
print(plate_stack)
