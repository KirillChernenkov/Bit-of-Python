with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task4.txt','w+') as file_4:
    line = input()
    file_4.writelines(line)
    my_numb = line.split()

print(sum(map(int, my_numb)))