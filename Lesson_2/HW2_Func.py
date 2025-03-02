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


#a,b = int(input()), int(input())
#task1_1(a,b)

#TASK2
#2.	Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def info():
    name,surname,birthday,city,email,tel = [input() for _ in range(6)]
    return print(f'Здравствуйте,{name} {surname}, дата рождения {birthday}, проживающий в городе {city}, email {email}, телефон {tel}')

#info()
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

#TASK5
#5.	Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def task_5():
    res = 0
    while True:
        numbers = input('Enter list of number or STOP to exit: ').split()
        for i in numbers:
            try:
                if i == 'STOP':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or STOP')
        print(f'Sum is {res}')

#task_5()

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

def domain_name_regex(s:str):
    domain = re.search('//([A-Za-z_0-9.-]+)[.]', s)
    return print(domain.group(1))

#domain_name_regex("http://google111212.com")

#TASK7
#7.	Написать функцию make_readable() принимающая количество секунд и возвращающая количество времени которое прошло HH:MM:SS.
# Секунды запрашивать у пользователя. Максимально возможное время в 359999 секундах  «99:99:99».
# Обработать условие сверх времени, если ввели 360000 или более то вывести «99:99:99», «00:00:00» и так для каждого круга сверх времени.

def make_readable(time_sec):
    h, m, s = int(), int(),int()
    h = time_sec // 3600
    m = (time_sec - h*3600) // 60
    s = time_sec % 60
    if time_sec>=360000:
        return print("99:99:99")
    else:
        return print(round(h),':',round(m), ':',round(s))

#sec = int(input())
#make_readable(sec)

#TASK8
#8.	Функция max_sequence() принимает массив (позиционный аргумент) заполненный рандомными числами в диапазоне от -100 до 100.
# Размера массива задается пользователем. Минимальный размер массива 10, если пользователь вводит число меньше 10,
# то по умолчанию размер массива 10
#Функция возвращает строку «Положительные победили» , если сумма положительных элементов больше чем  абсолютная сумма отрицательных элементов
# и «Отрицательные победили»  если  наоборот. Так же обработать возможность равной суммы и вывести «Все равны»

from random import randint

def max_sequence(n):
    a = []
    sum_pos = int()
    sum_neg = int()
    for i in range(0, n):
        a.insert(i, randint(-100, 100))
    print(*a)
    for i in range(0,n):
        if a[i]>0:
            sum_pos+=a[i]
        else:
            sum_neg+=a[i]
    if sum_pos>abs(sum_neg):
        return print("Положительные победили")
    else:
        return print("Отрицательные победили")

aa = int(input())
if aa<10:
    aa=10
max_sequence(aa)


