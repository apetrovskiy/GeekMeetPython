__author__ = 'Петровский А.Е.'

import os

def remove_dirs(name, number):
    root_path = os.getcwd()
    for i in range(1, number + 1):
        os.removedirs(root_path + "\\" + name + str(i))
