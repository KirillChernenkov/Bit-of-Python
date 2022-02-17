import os

#os.path.isdir("C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files")
b = open(r"task1.txt","w+")
print(b.name)
c = str()
while True:
    c = input()
    if c == '': break
    b.write(c)

b.close()
