"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(STR_VAL):
    dict_1 = {}
    for i in STR_VAL:
        dict_1.setdefault(i, 0)
        dict_1[i] += 1
    return dict_1


print(count_char(STR_VAL))
