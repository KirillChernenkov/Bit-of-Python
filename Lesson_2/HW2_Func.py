#TASK1
#1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# Использовать два варианта обработки деления на 0. Через if else и через try except

def new(x:int(),y:int()):
    while True:
        try:
            return x/y
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')



#a,b = int(input()), int(input())
#print(new(a,b))

#TASK3
#3.	Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# Обработать условие ввода строки
# Нельзя использовать функции max() min()

def my_func():
    a,b,c = [input() for _ in range(3)]
    if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
        print('Неправильный ввод')
    if (a>b)and(a>c)and(b>c):
        return print(int(a)+int(b))

my_func()