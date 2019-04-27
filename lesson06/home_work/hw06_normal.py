__author__ = 'Петровский А.Е.'


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Pupil:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class SchoolClass:
    def __init__(self, number, char, pupils):
        self.number = number
        self.char = char
        self._pupils = pupils

    def get_pupils(self):
        return list(map(lambda p: p.surname + " " + p.name[:1], self._pupils))

    @property
    def id(self):
        return self.number + self.char


class Teacher:
    def __init__(self, name, surname, classes):
        self.name = name
        self.surname = surname
        self.classes = classes


class Discipline:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, classes):
        self._classes = classes

    def get_classes(self):
        return list(map(lambda x: str(x.number) + x.char, self._classes))

    def get_class(self, class_id):
        return list(filter(lambda c: class_id == str(c.number) + c.char, self._classes))[0]


# classes
school = School((
    SchoolClass(1, 'a', (Pupil('Vasya', 'Poopkin'), Pupil('Ivan', 'Ivanov'))),
    SchoolClass(1, 'b', (Pupil('Masha', 'Pooplina'), Pupil('Joe', 'Smith'))),
    SchoolClass(2, 'a', (Pupil('Jack', 'Daniels'), Pupil('Kon', 'von Palto')))))

# 1
print(school.get_classes())

# 2
print(school.get_class('2a').get_pupils())

# 3


# 4


# 5



print('======================================================')
