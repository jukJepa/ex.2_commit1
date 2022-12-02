file = open("test.2", "r") #используем встроенную функцию open и с помощью режима "r" читаем файл
line_list = file.readlines() #значения из файла кладем в список, но они все воспринимаются как строка
for line in line_list:
    line_element = line.split() #поделим наши элементы, т.е. разобьем строку из элементов на части
    print("line_element = ", line_element)

for i in range(0, len(line_element)):
    locker = int(line_element[i]) #создали шкаф, в котором преобразовали все элементы строки в целочисленные (int)
    line_element[i] = locker #переобозначение переменной
print('line_element with number =', line_element)

L = line_element
for i in range(0, len(line_element)):
    for j in range(0, len(line_element)-i-1):
        if L[j+1] < L[j]:
            a = L[j]
            b = L[j+1]
            L[j] = b
            L[j+1] = a
print(line_element)
