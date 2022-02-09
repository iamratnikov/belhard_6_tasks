"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1):
    list_2 = []
    for i in list_1:
        if i not in list_2:
            print("No")
            list_2.append(i)
        else:
            print("Yes")


yes_or_no([1, 2, 3, 4, 3, 2])
