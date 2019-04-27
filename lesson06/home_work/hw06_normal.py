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
    def __init__(self, name, surname, class_id, mother, father):
        self.name = name
        self.surname = surname
        self.class_id = class_id
        self.mother = mother
        self.father = father

    def get_class(self):
        return self.class_id


class SchoolClass:
    def __init__(self, number, char, pupils, teachers):
        self.number = number
        self.char = char
        self._pupils = pupils
        self._teachers = teachers

    def get_pupils(self):
        return list(map(lambda p: p.surname + " " + p.name[:1], self._pupils))

    def get_pupil(self, name, surname):
        return list(filter(lambda p: name == p.name and surname == p.surname, self._pupils))[0]

    @property
    def id(self):
        return self.number + self.char

    def get_teachers(self):
        return list(map(lambda t: t.name + " " + t.surname, self._teachers))

    def get_teachers_with_disciplines(self):
        return list(map(lambda t: t.name + " " + t.surname + " " + t.discipline.name, self._teachers))


class Teacher:
    def __init__(self, name, surname, discipline):
        self.name = name
        self.surname = surname
        self.discipline = discipline


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
    SchoolClass(1, 'a',
                (Pupil('Vasya', 'Poopkin', '1a', 'Darya Poopkina', 'Edgar Poopkin'),
                 Pupil('Ivan', 'Ivanov', '1a', 'Elena Ivanova', 'Arkadiy Ivanov')),
                (Teacher('Ivan', 'Fedorov', Discipline('math')),
                 Teacher('Alex', 'Vasin', Discipline('pe')))),
    SchoolClass(1, 'b',
                (Pupil('Masha', 'Poopkina', '1b', 'Darya Poopkina', 'Edgar Poopkin'),
                 Pupil('Joe', 'Smith', '1b', 'Svetlana Smith', 'Richard Smith')),
                (Teacher('Sean', 'Russell', Discipline('math')),
                 Teacher('John', 'Smith', Discipline('pe')))),
    SchoolClass(2, 'a',
                (Pupil('Jack', 'Daniels', '2a', 'Sally Daniels', 'Arkadiy Ivanov'),
                 Pupil('Kon', 'von Palto', '2a', 'Maria Elisabeth von Palto', 'Artur von Palto')),
                (Teacher('Kim', 'Yang', Discipline('english')),
                 Teacher('Won', 'Tun', Discipline('korean'))))))

# 1. Получить полный список всех классов школы
print(school.get_classes())

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print(school.get_class('2a').get_pupils())

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
pupil = school.get_class('1a').get_pupil('Vasya', 'Poopkin')
print(pupil.class_id)
print(pupil.surname, ':', school.get_class(pupil.class_id).get_teachers_with_disciplines())

# 4. Узнать ФИО родителей указанного ученика
print(pupil.surname, ':', pupil.mother, ',', pupil.father)

# 5. Получить список всех Учителей, преподающих в указанном классе
print('1a', school.get_class('1a').get_teachers())
print('1b', school.get_class('1b').get_teachers())
print('2a', school.get_class('2a').get_teachers())

print('======================================================')
