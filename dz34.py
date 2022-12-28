# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def reverse_string2(s):
    return "".join(reversed(s))

file1=open("file341.txt","r")
list_num1=file1.readline()
file2=open("file342.txt","r")
list_num2=file2.readline()
file1.close()
file2.close()

list_sum=str()
list_num1=reverse_string2(str(list_num1))
list_num2=reverse_string2(str(list_num2))

print(list_num1)
print(list_num2)

list_num1=(list_num1.translate({ord(i): None for i in '0='}))
list_num2=(list_num2.translate({ord(i): None for i in '0='}))

list_of_poly_1 = list_num1.split()
list_of_poly_2 = list_num2.split()

res_dict1 = dict((a.strip(), int(b.strip())) 
                     for a, b in(element.split('^x*') 
                                  for element in list_num1.split('+'))) 
res_dict=res_dict1.copy()

res_dict2 = dict((a.strip(), int(b.strip())) 
                     for a, b in(element.split('^x*') 
                                  for element in list_num2.split('+'))) 

for key, val in res_dict2.items():
    res_dict[key] = res_dict.get(key, 0) + val
print(res_dict)

ip=0
for key, val in res_dict.items():
    if ip==0:
        list_sum+=str(f"{val}*x^{key}")
    else:
        list_sum+=str(f"+{val}*x^{key}")
    ip+=1
list_sum+=str("=0")
filesum = open('filesum.txt', 'w')
filesum.writelines(list_sum)
filesum.close()






# ln2=res_dict
# for item in res_dict.items():
#     ln2=(item[0], item[1])
    # item — это кортеж (ключ, значение)
    

# d1 = {4: 150, 'b': 'Hello ', 3: 100}
# d2 = {1: 50, 'b': 'world', 3: 100}
# d = d1.copy()
# for k, v in d2.items():
#     d[k] = d.get(k, 0) + v
# print(d)




# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')