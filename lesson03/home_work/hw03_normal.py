__author__ = 'Петровский А.Е.'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def fibonacci_number(n):
        if 2 > n:
            return n
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)

    result_list = list(map(lambda x: fibonacci_number(x), range(n, m + 1)))
    return result_list


print([2, 3, 5, 8] == fibonacci(3, 6))
print([1] == fibonacci(1, 1))
print([1, 1] == fibonacci(1, 2))
print([1, 1, 2] == fibonacci(1, 3))
print([55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765] == fibonacci(10, 20))
print('===============================================================')


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

print('===============================================================')

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('===============================================================')


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# A1A2 == A3A4 and A2A3 == A1A4

# A2    A3

# A1    A4

def is_parallelogram(**kwargs):
    def get_x(coordinates):
        return coordinates[0]

    def get_y(coordinates):
        return coordinates[1]

    def get_horizontal_line_length(coordinates1, coordinates2):
        return get_x(coordinates2) - get_x(coordinates1)

    def get_vertical_line_length(coordinates1, coordinates2):
        return get_y(coordinates2) - get_y(coordinates1)

    horizontal_equality = get_horizontal_line_length(kwargs["A2"], kwargs["A3"]) == get_horizontal_line_length(
        kwargs["A1"], kwargs["A4"])
    vertical_equality = get_vertical_line_length(kwargs["A2"], kwargs["A1"]) == get_vertical_line_length(kwargs["A3"],
                                                                                                         kwargs["A4"])
    if horizontal_equality and vertical_equality:
        return True
    return False


print(True == is_parallelogram(A1=[1, 1], A2=[2, 3], A3=[5, 3], A4=[4, 1]))
print(False == is_parallelogram(A1=[1, 1], A2=[2, 3], A3=[5, 2], A4=[4, 1]))

print('===============================================================')
