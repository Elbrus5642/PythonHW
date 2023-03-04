'''Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 '''
number_a =int(input('Введите число, которое является основанием степени: ''\n'))
number_b =int(input('Введите число, которое является показателем степени: ''\n'))
print(f'Основание степени - число: {number_a}')
print(f'Показатель степени - число: {number_b}''\n')

def degree_num(a,b):
     if b == 0:
        return 1
     else:
        b -=1
        return int(a * degree_num(a, b))
print(f'Число {number_a} в степени {number_b}: {degree_num(number_a, number_b)}')     
#print(degree_num(number_a, number_b))