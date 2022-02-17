with open(r'task4.txt','w+') as file_4:
    digits = [12121,2222,3,4,511]    
    bb = sum(digits)
    file_4.writelines(str(bb))  
