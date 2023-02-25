'''Задаем длину списка наполненного рандомными числами от 1 до 100. Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению'''
import random
import math
print('Введите число, которое будет сравниваться с элементами списка:')
number_x = int(input())
print('Введите число, определяющее длину списка:')
list_length = int(input())
list_1 = [random.randint(1, 100) for i in range(list_length)]
print(*list_1)
count = 0
for i in range(len(list_1)):
    if list_1[i] == number_x:
        count += 1
print(f'В списке число {number_x} встречается: {count} раз')
if count == 0:
    list_2 = [abs(list_1[i]-number_x) for i in range(len(list_1))]
    print(f'Спиок разностей элементов списка и заданного числа {number_x}:')
    print(*list_2)
    min_el = list_2[0]
    index_min = 0
    for i in range(len(list_2)):
        if list_2[i] < min_el:
            min_el = list_2[i]
            index_min = i

    print(f'Максимально близкое число к заданному числу из списка: {list_1[index_min]}\n Разница между заданным числом и ближайшим к нему: {min_el}')
