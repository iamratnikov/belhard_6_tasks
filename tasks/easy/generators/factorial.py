"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    num_1 = 1
    num_2 = 1
    while True:
        num_1 *= num_2
        yield num_1
        num_2 += 1


fac = factorial()
print(next(fac))
