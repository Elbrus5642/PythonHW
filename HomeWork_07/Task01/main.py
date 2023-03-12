# Задача про Винни Пуха и кричалки

frase_1 ='пара-ра-рам рам-пам-папам па-ра-па-да'
print(frase_1)
frase_2 = 'Парам пам-пам'
frase_3 = 'Пам парам'
list_glas =['а', 'е', 'и', 'ё', 'о', 'у', 'э', 'ю', 'я']
list_of_conts = []

frase_to_list_1 = frase_1.split(' ')
#print(type(frase_to_list_1))
print(frase_to_list_1)

for item in frase_to_list_1:
    print(f'Фраза: {item}''\n')
    count_glas = 0
    for j in (item):
            if j == 'а': 
               #or item[j] =='е' or  item[j] == 'и' or item[j] == 'ё' or item[j] == 'о' or item[j] == 'у' or item[j] == 'э' or item[j] == 'ю' or item[j] == 'я':
               #print('гласные есть') 
               count_glas +=1
            #else:
                #print('гласных нет')
    #print(count)
    list_of_conts.append(count_glas)
print(f'Количество гласных во фразах:' '\t'f'{list_of_conts}')
# Завершение задачи про кричалки Винни Пуха: две концовки
'''if list_of_conts[0]!= list_of_conts[1]:
     print(frase_2)
else:
     print(frase_3)'''
list_of_conts = set(list_of_conts)
if len(list_of_conts) != 1:
     print('Условие не выполнено:''\t' f'{frase_3}')
else:
     print('Условие выполнено:''\t' f'{frase_2}')
