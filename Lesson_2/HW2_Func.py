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

#my_func()

#TASK4
#4.	Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполнить возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень pow()
# Попробовать решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй - реализация без оператора **, предусматривающая использование цикла.

def my_func1(xx:int,yy:int):
   return print(xx**yy)

def my_func11(xx:int,yy:int):
   ans = xx
   for i in range(1,yy):
       ans = ans*xx
   return print(ans)


#a,b = int(input()),int(input())
#my_func11(a,b)


#TASK6
#Реализовать функцию domain_name() которая принимает название сайта (позиционный аргумент) и возвращает только название домена.
# Реализовать двумя способами , с регулярными выражениями и без них
# domain_name("http://google.com") return "google"

def domain_name(s:str):
    y = int()
    ss = str()
    for x in range(len(s)):
        if s[x]=='/' and s[x+1]!='/':
            y = x
    for x in range(y+1,len(s)):
        ss = ss + s[x]
        if s[x + 1] == '.':
            break
    return print(ss)

domain_name("http://yandex.com")


