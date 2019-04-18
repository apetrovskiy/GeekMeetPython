__author__ = 'Петровский А.Е.'


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    remainder = number - int(number)
    return remainder


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print(2.12346 == my_round(2.1234567, 5))
print(2.2 == my_round(2.1999967, 5))
print(3.0 == my_round(2.9999967, 5))
print('===============================================================')


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    first_part = int(ticket_number / 1000)
    last_part = ticket_number - first_part * 1000

    def sum_of_digits(number):
        hundreds = int(number / 100)
        tens = int((number - hundreds * 100) / 10)
        return hundreds + tens + (number - hundreds * 100 - tens * 10)

    return sum_of_digits(first_part) == sum_of_digits(last_part)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(111111))
print(lucky_ticket(123456))
print(lucky_ticket(125))
print(lucky_ticket(0))
print(lucky_ticket(-1))
print('===============================================================')
