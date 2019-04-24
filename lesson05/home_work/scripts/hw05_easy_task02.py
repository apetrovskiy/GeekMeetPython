__author__ = 'Петровский А.Е.'

import os

root_path = os.getcwd();

for r, d, f in os.walk(root_path):
    print(d)
