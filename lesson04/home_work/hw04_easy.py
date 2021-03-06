__author__ = 'Петровский А.Е.'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

source_list = [1, 2, 4, 0]
expected_list = [1, 4, 16, 0]


def squadratize(input_list):
    return [el ** 2 for el in input_list]


print(expected_list == squadratize(source_list[:]))
source_list.append(2)
expected_list_01 = expected_list[:]
expected_list_01.append(2);
print(expected_list_01 != squadratize(source_list[:]))
expected_list_02 = expected_list[:]
expected_list_02.append(4)
print(expected_list_02 == squadratize(source_list[:]))
print('===============================================================')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_001 = ['яблоко', 'груша', 'айва', 'манго']
list_002 = ['яблоко', 'папайя', 'манго']


def get_common_items(list01, list02):
    return [el for el in list01 if list02.__contains__(el)]


print(get_common_items(list_001, list_002))
print('===============================================================')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
source_list = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def get_number_by_rules(list01):
    return [el for el in list01 if 0 == el % 3 and el > 0 and 0 != el % 4]


print([3, 6, 9] == get_number_by_rules(source_list))
print('===============================================================')
