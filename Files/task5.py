subjects = {}
with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task5.txt','r', encoding='utf-8') as file5:
    lines = file5.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        subjects[data[1][:-1]] = sum(int(i) for i in data if i.isdigit())

print(subjects)