#TASK8
#8.	Функция max_sequence() принимает массив (позиционный аргумент) заполненный рандомными числами в диапазоне от -100 до 100.
# Размера массива задается пользователем. Минимальный размер массива 10, если пользователь вводит число меньше 10,
# то по умолчанию размер массива 10
#Функция возвращает строку «Положительные победили» , если сумма положительных элементов больше чем  абсолютная сумма отрицательных элементов
# и «Отрицательные победили»  если  наоборот. Так же обработать возможность равной суммы и вывести «Все равны»

from random import randint

def max_sequence(a:[],n):
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

nn = int(input())
mas = []

if nn<10:
    nn=10
max_sequence(mas,nn)