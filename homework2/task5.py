# -*- coding:utf-8 -*-

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

user_rate = int(input('Введите новый элемент рейтинга: '))

my_list = [7, 5, 3, 3, 2]

currentIndex = None
for index, num in enumerate(my_list):
    if user_rate > num:
        currentIndex = index
        break

if currentIndex == None:
    my_list.insert(len(my_list), user_rate)
else:
    my_list.insert(currentIndex, user_rate)

print(my_list)