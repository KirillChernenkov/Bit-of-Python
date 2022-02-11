import os

#os.path.isdir("C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files")
b = open(r"C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task1.txt","w+")
print(b.name)
b.write('HEllO')
b.write('HEllO')
b.close()