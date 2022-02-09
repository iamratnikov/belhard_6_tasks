"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    i = 2
    while True:
        yield i
        i += 2


e_g = get_even_number()

print(next(e_g))
