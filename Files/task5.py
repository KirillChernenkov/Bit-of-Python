subjects = {}
with open(r'task5.txt','r', encoding='utf-8') as file5:
    lines = file5.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        for x in data:
            subjects1 = sum(int(i) for i in data if i.isdigit())
            subjects.update({data[0]:subjects1})
    print(subjects)
