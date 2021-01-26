"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter


class Tree:
    """Максимально простой класс дерева"""
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def build_tree(string):
    """Функция возвращает дерево Хаффмана по переданной строке"""
    counter = Counter(string)  # Считаем как часто встречаются символы
    if len(counter) == 1:
        return string[0]
    while len(counter) != 1:
        a, b = counter.most_common()[-2:]  # Выбираем два элемента, которые имеют минимальную частоту
        # Создаем дерево, корнем которого является сумма частот этих элементов, а ответвлениями -
        # символ который нужно закодировать (если это листок) или другое дерево
        huffman_tree = Tree(a[1] + b[1], a[0], b[0])
        # Заменяем эти два элемента на дерево, даём ему частоту равную сумме частот элементов (корень дерева)
        del counter[a[0]]
        del counter[b[0]]
        counter[huffman_tree] = huffman_tree.root
        # И так до тех пор пока не останется одного элемента в counter, это означает, что дерево построено
    return list(counter.keys())[0]  # Возвращаем дерево


def read_tree(huffman_tree, dictionary=None, s=''):
    """Рекурсивная функция, которая "читает" дерево и возвращает словарь, содержащий коды для шифрования строки"""
    if dictionary is None:
        dictionary = dict()
    # Условие выполняется, если рекурсиная функция дошла до листка (символа)
    if isinstance(huffman_tree, str):
        dictionary[huffman_tree] = s  # В таком случае добавляем в словарь под ключом символа его код
        return {huffman_tree: '1'}  # Без этого не получится получить коды Хаффмана если в исходной строке 1 символ
    read_tree(huffman_tree.left, dictionary, s + '0')  # Если идём в левую ветку от корня, то добавляем к коду 0
    read_tree(huffman_tree.right, dictionary, s + '1')  # В правую - 1. На самом неважно, можно и наоборот
    return dictionary


def decode(string, dictionary):
    """Функция, которая принимает закодированную строку, а также коды Хаффмана, по которым ее можно расшифровать и
    возвращает декодированную строку"""
    reversed_dictionary = {value: key for key, value in dictionary.items()}
    res = s = ''
    for sym in string:
        s += sym
        decoded = reversed_dictionary.get(s)
        if decoded is not None:
            res += decoded
            s = ''
    return res


source_string = 'Beep Beep I am Jeep'

tree = build_tree(source_string)
codes = read_tree(tree)

new_string = ''
for el in source_string:
    new_string += codes[el]

print('Исходная строка:', source_string)
print('Словарь кодов Хаффмана:', codes)
print('Закодированная строка:', new_string)
print('Декодированная строка:', decode(new_string, codes))
