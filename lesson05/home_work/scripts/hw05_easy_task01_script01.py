__author__ = 'Петровский А.Е.'

import os

root_path = os.getcwd();

for i in range(1, 10):
    os.makedirs(root_path + "\\dir" + str(i))

print(os.listdir(root_path))
