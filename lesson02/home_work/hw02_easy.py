__author__ = 'Петровский А.Е.'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
max_word_length = 0
word_number = 0;

while word_number < len(fruit_list):
    current_word_length = len(fruit_list[word_number])
    if current_word_length > max_word_length:
        max_word_length = current_word_length
    word_number += 1

word_number = 0
while word_number < len(fruit_list):
    needed_spaces_number = max_word_length - len(fruit_list[word_number])
    spaces = " " * needed_spaces_number
    print('{0}{1}'.format(spaces, fruit_list[word_number]))
    word_number += 1
print("===============================================")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_001 = ['aaa', 'bbb', [1, 2, 3], 4, 5]
list_002 = ['aaa', 'ccc', [1, 2, 3], 5, 6]
item_number = 0

while item_number < len(list_001):
    if list_002.__contains__(list_001[item_number]):
        list_001.remove(list_001[item_number])
    item_number += 1

for item in list_001:
    print(item)
print("===============================================")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = []
item_number = 0

while item_number < len(list_of_numbers):
    if 1 < list_of_numbers[item_number] and 0 == list_of_numbers[item_number] % 2:
        result_list.append(list_of_numbers[item_number] / 4)
    else:
        result_list.append(list_of_numbers[item_number] * 2)
    item_number += 1

for item in result_list:
    print(item)
print("===============================================")