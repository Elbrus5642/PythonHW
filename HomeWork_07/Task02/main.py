'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.'''

number_x = int(input('Введите число  х: '))
number_y = int(input('Введите число  y: '))
print(f'Число столбцов таблицы: {number_x}''\n' f'Число строк таблицыЖ {number_y}')
# Функция: произведение двух чисел
multy_num = lambda x,y: x * y
print(f'Произведение  х*у равно: {multy_num(number_x,number_y)}')
# Функция: вывод на печать матрицы размером Х на У: 
def print_operation_table (func,x,y):
    for i in range(1, x + 1):
        list_1 = []
        for j in range(1, y + 1):
              list_1.append(func(i,j))
        print(*list_1, end ='\n')

print_operation_table(multy_num, number_x, number_y)    