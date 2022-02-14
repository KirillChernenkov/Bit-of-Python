import requests as requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

#Создать текстовый файл (не программно), сохранить в нем текст по ссылке https://ilibrary.ru/text/69/p.2/index.html
link='https://ilibrary.ru/text/69/p.2/index.html'
lines = int()
page = urlopen(link)
soup = BeautifulSoup(page.read(), 'html.parser')
body  = ''.join([line.text for line in soup])
with open(r'task_5.txt','w',encoding='utf-8') as file:
    file.write(body)

#Task0
#выполнить подсчёт строк
for line in body:
    if line=='\n':
        lines += 1
print('Количество строк в тексте-',lines)

#Task1
#Создать дата фрейм который содержит один столбец. Этот столбец должен содержать все слова и букры которе встречаются в тексте
df = pd.DataFrame()
words = body.split()
words_new = []
for x in words:
    x = x.rstrip('.,;:?!«()-')
    words_new.append(x)


df['Words'] = words_new
#print(df.head(7))

#Task2
#Создать дата фрейм который показывает сколько какое слово встречается в списке
df1 = pd.DataFrame()
words_dict = get_words_dict(words_new)
for key,value in words_dict.items():
    df1['Words1'] = words_dict.keys()
    df1['Values'] = words_dict.values()

#print(df1.head(7))

#Task3
#Вывести общее количество слов в тексте
print('Количество слов в тексте-',len(words_new))

#Task4
#Вывести количество уникальных слов в тексте
print('Количество уникальных слов в тексте-',len(words_dict))

#Task5
#Посчтитать процент уникальзых слов от общего количества
print('процент уникальзых слов от общего количества-',100*(len(words_dict))/(len(words_new)),'%')



