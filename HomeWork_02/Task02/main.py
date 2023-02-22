'''Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
import random
print('Случайно выбираются два числа "Х" и "У" (по условию задачи они неизвестны)')
number_x =  random.randint(1,5)
#print(f'Первое число "Х" = {number_x} ')
number_y = random.randint(1,5)
#print (f'Второе число "У" = {number_y} ')
sum = number_x + number_y
multi = number_x * number_y
temp_sum = 0
temp_multi = 0
num_x = 0
num_y = 0
print(F'Сумма двух чисел равна: {sum} \nПроизведение двух чисел равно: {multi}')
for i in range(1,6):
       for j in range(1,6):
           temp_sum = i + j
           temp_multi = i * j
           if (temp_sum == sum)and(temp_multi == multi):
                 num_x = i
                 num_y  = j    
print(f'Первое число "Х" = {num_x} , второе число "У" = {num_y}')
