with open(r'task2.txt','r') as new_file:
    salary = []
    answer = []
    list1 = new_file.read().split('\n')
    for x in list1:
        x = x.split()
        if int(x[1])<20000:
            answer.append(x[0])
        salary.append(x[1])

print('Оклад меньше 20000', answer)
print('Средний оклад', sum(map(int,salary))/len(list1))
