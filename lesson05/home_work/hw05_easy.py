__author__ = 'Петровский А.Е.'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import lesson05.home_work.scripts.hw05_easy_task01_script01 as task01script01
import lesson05.home_work.scripts.hw05_easy_task01_script02 as task01script02

task01script01.create_dirs('dirr', 9)
task01script02.remove_dirs('dirr', 9)

print('==================================================================')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import lesson05.home_work.scripts.hw05_easy_task02 as task02

task02.print_dirs()

print('==================================================================')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import lesson05.home_work.scripts.hw05_easy_task03 as task03

task03.copy_file_content()

print('==================================================================')