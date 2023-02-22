'''Требуется вывести все целые степени двойки (т.е. числа
вида 2k ), не превосходящие числа N : 10 -> 1 2 4 8'''
import random
print("Вводится случайное число от 1 до 100:")
number = random.randint(1,100)
print(F'Целые степени "двойки" не превосходящие {number} ->:')
degree_two = 0

while 2**degree_two < number:
    if 2**degree_two == 1:
        print (f'{number} ->',2**degree_two, end =" " )
    else:
        print (2**degree_two, end =" " )
    degree_two +=1