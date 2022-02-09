"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(x):
    if x == 0:
        return 0
    else:
        return x % 10 + sum_of_numbers(x // 10)


print(sum_of_numbers(1234))
