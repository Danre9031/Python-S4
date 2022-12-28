# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
list_num= "1, 2, 4, 5, 5"
print(f'[{list_num}]')
list_end=[]
for i in list_num:
    if list_num.count(i)==1:
        list_end.append(i)
print(f'список неповторяющихся чисел {list(map(int,list_end))}')
