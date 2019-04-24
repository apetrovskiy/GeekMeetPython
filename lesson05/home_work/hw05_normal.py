__author__ = 'Петровский А.Е.'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import lesson05.home_work.hw05_easy as easy


# easy.task01script01
# easy.task01script02
# easy.task02
# easy.task03

def help():
    print("help  - getting help")
    print("cd    - go to a folder")
    print("ls    - list files and subfolders")
    print("rmdir - remove a folder")
    print("mkdir - create a folder")


def ls(path_to_dir):
    try:
        print(os.listdir(path_to_dir))
    except FileNotFoundError:
        print("Directory {} does not exist or inaccessible".format(path_to_dir))


def rmdir():
    try:
        easy.task01script02.remove_dirs(dir_name, 1)
    except:
        print("Directory {} does not exist or inaccessible".format(path_to_dir))


def mkdir():
    try:
        easy.task01script01.create_dirs(dir_name, 1)
    except:
        print("Directory {} does not exist or inaccessible".format(path_to_dir))


do = {
    "help": help,
    # "cd": cd,
    "ls": ls,
    "rmdir": rmdir,
    "mkdir": mkdir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        help()

print('==================================================================')
