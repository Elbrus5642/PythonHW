'''Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random
number_el = int(input('Введите количество элементов списка: '))
mini_point= int(input('Введите минимальное значение интервала: '))
maxi_point = int(input('Введите максимальное значение интервала: '))
list_1 =[random.randint(1, 50) for i in range(number_el)]
list_2 =[]
list_3 = []
print(f'{list_1}')
for i  in range(number_el):
    if  mini_point <= list_1[i] <= maxi_point:
        list_2.append(i)
        list_3.append(list_1[i])
print(f'Список индексов элементов в диапазоне от {mini_point} до {maxi_point}:')
print(*list_2)
print(f'Список элементов в диапазоне от {mini_point} до {maxi_point}:')
print(list_3)

