'''Напишите рекурсивную функцию sum(a, b),
 возвращающую сумму двух целых неотрицательных чисел. 
 Из всех арифметических операций допускаются только +1 и -1.
   Также нельзя использовать циклы.'''

number_a  = int(input('Введите число А: '))
number_b  = int(input('Введите число В: '))

def sum_two_num(a,b):
     a +=1
     b -=1
     if b < 0:
        return a
     else:
        return sum_two_num(a,b)
print(f'Сумма {number_a} и {number_b} равна {sum_two_num(number_a, number_b)-1}')