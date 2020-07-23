
__author__ = 'Петровский А.Е.'
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
var_number = 2343201
var_extent = 20
var_start_printing = False
var_max_digit = 0

while var_extent >= 0:
    var_digit = int(var_number / 10 ** var_extent)
    if var_number >= 10 ** var_extent:
        var_start_printing = True
    var_number = var_number - var_digit * 10 ** var_extent
    var_extent -= 1
    if var_start_printing:
        if var_digit > var_max_digit:
            var_max_digit = var_digit

print(var_max_digit)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# this works only for numbers!
var_1 = int(input("input value 1"))
var_2 = int(input("input value 2"))
print("var_1 = ", var_1)
print("var_2 = ", var_2)
var_1 += var_2
var_2 = var_1 - var_2
var_1 = var_1 - var_2
print("var_1 = ", var_1)
print("var_2 = ", var_2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

var_a = int(input("Введите первый член"))
var_b = int(input("Введите второй член"))
var_c = int(input("Введите третий член"))
var_d = var_b ** 2 - 4 * var_a * var_c

print("Корень 1: ", (-var_b + math.sqrt(var_d))/ 2 / var_a)
print("Корень 2: ", (-var_b - math.sqrt(var_d))/ 2 / var_a)
