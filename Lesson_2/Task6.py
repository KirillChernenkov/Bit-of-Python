import re

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

a = input()
domain_name_regex(a)