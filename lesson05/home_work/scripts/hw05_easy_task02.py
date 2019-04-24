__author__ = 'Петровский А.Е.'

import os

def print_dirs():
    root_path = os.getcwd()
    for r, d, f in os.walk(root_path):
        print(d)
