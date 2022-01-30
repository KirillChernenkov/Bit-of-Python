import re

#TASK1
#1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# Использовать два варианта обработки деления на 0. Через if else и через try except

def task1_1(x,y):
    if y==0:
        print(f'Ошибка! Делить на ноль нельзя')
    else:
        return print(x/y)


def task1_2(x,y):
    try:
        return print(x/y)
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')


a,b = int(input()), int(input())
task1_1(a,b)