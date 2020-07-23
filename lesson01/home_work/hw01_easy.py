
__author__ = 'Петровский А.Е.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
# variant 01
var_number = 2343201
var_extent = 20
var_start_printing = False

while var_extent >= 0:
    var_digit = int(var_number / 10 ** var_extent)
    if var_number >= 10 ** var_extent:
        var_start_printing = True
    var_number = var_number - var_digit * 10 ** var_extent
    var_extent -= 1
    if var_start_printing:
        print(var_digit)

# variant 02
var_number = 2343201
var_number_as_string = str(var_number)
var_length = len(var_number_as_string)
i = 0

while i < var_length:
    print(var_number_as_string[i])
    i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

var_1 = input("input value 1")
var_2 = input("input value 2")
print("var_1 = ", var_1)
print("var_2 = ", var_2)
var_temp = var_1
var_1 = var_2
var_2 = var_temp
print("var_1 = ", var_1)
print("var_2 = ", var_2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

var_age = int(input("Введите ваш возраст, лет"))
if var_age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")