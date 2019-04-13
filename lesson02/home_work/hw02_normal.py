__author__ = 'Петровский А.Е.'

import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
list_001 = [2, -5, 8, 9, -25, 25, 4]
list_002 = []

for item in list_001:
    if item >= 0:
        square_root = math.sqrt(item)
        if square_root // 1 == square_root:
            list_002.append(int(square_root))

print(list_002)
print('===================================')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date = "31.10.1999"
#"30.07.2001"
#"24.09.2003"
#"20.12.2005"
#"15.04.2010"
#"10.01.1985"
#""02.11.2013"

day = date[:2]
day_last_digit = int(date[1:2])
day_first_digit = int(date[0:1])
day_number = int(day)
month_number = int(date[3:5])
day_word = "первое"
month_word = "января"

if 2 == day_last_digit:
    day_word = "второе"
elif 3 == day_last_digit:
    day_word = "третье"
elif 4 == day_last_digit:
    day_word = "четвёртое"
elif 5 == day_last_digit:
    day_word = "пятое"
elif 6 == day_last_digit:
    day_word = "шестое"
elif 7 == day_last_digit:
    day_word = "седьмое"
elif 8 == day_last_digit:
    day_word = "восьмое"
elif 9 == day_last_digit:
    day_word = "девятое"

if 2 == day_first_digit:
    day_word = "двадцать " + day_word
elif 3 == day_first_digit:
    day_word = "тридцать " + day_word

if 10 == day_number:
    day_word = "десятое"
elif 11 == day_number:
    day_word = "одиннадцатое"
elif 12 == day_number:
    day_word = "двенадцатое"
elif 13 == day_number:
    day_word = "тринадцатое"
elif 14 == day_number:
    day_word = "четырнадцатое"
elif 15 == day_number:
    day_word = "пятнадцатое"
elif 16 == day_number:
    day_word = "шестнадцатое"
elif 17 == day_number:
    day_word = "семнадцатое"
elif 18 == day_number:
    day_word = "восемнадцатое"
elif 19 == day_number:
    day_word = "девятнадцатое"
elif 20 == day_number:
    day_word = "двадцатое"
elif 30 == day_number:
    day_word = "тридцатое"

if 2 == month_number:
    month_word = "февраля"
elif 3 == month_number:
    month_word = "марта"
elif 4 == month_number:
    month_word = "апреля"
elif 5 == month_number:
    month_word = "мая"
elif 6 == month_number:
    month_word = "июня"
elif 7 == month_number:
    month_word = "июля"
elif 8 == month_number:
    month_word = "августа"
elif 9 == month_number:
    month_word = "сентября"
elif 10 == month_number:
    month_word = "октября"
elif 11 == month_number:
    month_word = "ноября"
elif 12 == month_number:
    month_word = "декабря"

result = day_word + " " + month_word + " " + date[6:10] + " года"

print(result)

print('===================================')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

number_of_elements = 55
counter = 1
result_list = []
random.seed = 1

while counter <= number_of_elements:
    result_list.append(random.randint(-100, 100))
    counter += 1

print(result_list)
print('===================================')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
result_list_1 = list(set(lst))
print(result_list_1)

result_list_2 = []
for item in lst:
    if 1 == lst.count(item):
        result_list_2.append(item)
print(result_list_2)

print('===================================')