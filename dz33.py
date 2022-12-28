# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

num=int(input("Введите натуральную степень k: "))
list_num_random=[random.randint(0,100) for i in range(0,num+1)]
list_x=(f"{list_num_random[0]}*x^{num}")

print(list_num_random)

for i in list_num_random[1:]:
    num-=1
    if i == 0:
        list_x=list_x
    else:
        if i != list_num_random[-1]:
            list_x+=(f"+{i}*x^{num}")
        else:
            list_x+=(f"+{i}=0")
        
data = open('file.txt', 'w')
data.writelines(list_x)
data.close()
