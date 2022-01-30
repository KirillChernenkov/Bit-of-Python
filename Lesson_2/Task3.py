#TASK3
#3.	Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# Обработать условие ввода строки
# Нельзя использовать функции max() min()

def my_func():
    def maxx(a:int,b:int):
        if a>b:
            return a
        else:
            return b
    a,b,c = [input() for _ in range(3)]
    if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
        print('Неправильный ввод')
    return print(int(maxx(a,b))+int(maxx(b,c)))

my_func()