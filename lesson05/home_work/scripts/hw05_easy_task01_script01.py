__author__ = 'Петровский А.Е.'

import os

def create_dirs(name, number):
    root_path = os.getcwd()
    for i in range(1, number + 1):
        os.makedirs(root_path + "\\" + name + str(i))
