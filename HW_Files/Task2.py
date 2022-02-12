
with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task2.txt','r') as new_file:
    salary = []
    answer = []
    list = new_file.read().split('\n')
    for x in list:
        x = x.split()
        if int(x[1])<20000:
            answer.append(x[0])
        salary.append(x[1])

print('Оклад меньше 20000', answer)
print('Средний оклад', sum(map(int,salary))/10)
