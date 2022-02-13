arr = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task3.txt','r') as file_3:
    for i in file_3:
        i = i.split(' ', 1)
        new_file.append(arr[i[0]] + '  ' + i[1])

with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task3_new.txt','w') as file_3_new:
    file_3_new.writelines(new_file)