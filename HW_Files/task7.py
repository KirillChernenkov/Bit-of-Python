results = [{}, {}]

with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task7.txt','r', encoding='utf-8') as fhs:
    lines = fhs.readlines()

for line in lines:
    name, _, proceeds, expenses = line.split()
    results[0][name] = int(proceeds) - int(expenses)
    results[1]['average_profit'] = round(sum(profit for _, profit in results[0].items() if profit > 0)/len(results[0]))

with open(r'C:\Users\Admin\PycharmProjects\Bit-of-Python\HW_Files\task7_ans.txt', "w", encoding='utf-8') as fhd:
    fhd.write(str(results))
