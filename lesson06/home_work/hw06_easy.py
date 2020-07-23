__author__ = 'Петровский А.Е.'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_length(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def get_perimeter(self):
        return self.get_length(self.a, self.b) + self.get_length(self.b, self.c) + self.get_length(self.c, self.a)

    def get_square(self):
        pp = self.get_perimeter() / 2
        ab = self.get_length(self.a, self.b)
        bc = self.get_length(self.b, self.c)
        ca = self.get_length(self.c, self.a)
        return math.sqrt(pp * (pp - ab) * (pp - bc) * (pp - ca))

    def get_height(self):
        return self.get_square() * 2 / self.get_length(self.a, self.b)


# a classic square-angled triangle
triangle01 = Triangle((1, 1), (1, 4), (5, 1))
print(triangle01.get_length(triangle01.a, triangle01.b))
print(triangle01.get_length(triangle01.b, triangle01.c))
print(triangle01.get_length(triangle01.c, triangle01.a))
print(triangle01.get_perimeter())
print(triangle01.get_square())
print(triangle01.get_height())
print('===================')

triangle02 = Triangle((-1, -1), (1, 4), (5, 1))
print(triangle02.get_length(triangle02.a, triangle02.b))
print(triangle02.get_length(triangle02.b, triangle02.c))
print(triangle02.get_length(triangle02.c, triangle02.a))
print(triangle02.get_perimeter())
print(triangle02.get_square())
print(triangle02.get_height())

print('======================================================')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_length(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def get_perimeter(self):
        return self.get_length(self.a, self.b)\
               + self.get_length(self.b, self.c)\
               + self.get_length(self.c, self.d)\
               + self.get_length(self.d, self.a)

    def get_square(self):
        h = self.b[1] - self.a[1]
        return (self.get_length(self.b, self.c) + self.get_length(self.d, self.a)) / 2 * h

    def is_symmetric(self):
        return self.get_length(self.a, self.b) == self.get_length(self.c, self.d)


# a rectangle
trapezoid01 = Trapezoid((1, 1), (1, 4), (5, 4), (5, 1))
print(trapezoid01.get_length(trapezoid01.a, trapezoid01.b))
print(trapezoid01.get_length(trapezoid01.b, trapezoid01.c))
print(trapezoid01.get_length(trapezoid01.c, trapezoid01.d))
print(trapezoid01.get_length(trapezoid01.d, trapezoid01.a))
print(trapezoid01.get_perimeter())
print(trapezoid01.get_square())
print(trapezoid01.is_symmetric())
print('===================')

# a symmetric trape
trapezoid02 = Trapezoid((1, 1), (3, 4), (5, 4), (7, 1))
print(trapezoid02.get_length(trapezoid02.a, trapezoid02.b))
print(trapezoid02.get_length(trapezoid02.b, trapezoid02.c))
print(trapezoid02.get_length(trapezoid02.c, trapezoid02.d))
print(trapezoid02.get_length(trapezoid02.d, trapezoid02.a))
print(trapezoid02.get_perimeter())
print(trapezoid02.get_square())
print(trapezoid02.is_symmetric())
print('===================')

# an asymmetric trape
trapezoid03 = Trapezoid((1, 1), (3, 4), (4, 4), (7, 1))
print(trapezoid03.get_length(trapezoid03.a, trapezoid03.b))
print(trapezoid03.get_length(trapezoid03.b, trapezoid03.c))
print(trapezoid03.get_length(trapezoid03.c, trapezoid03.d))
print(trapezoid03.get_length(trapezoid03.d, trapezoid03.a))
print(trapezoid03.get_perimeter())
print(trapezoid03.get_square())
print(trapezoid03.is_symmetric())

print('======================================================')
