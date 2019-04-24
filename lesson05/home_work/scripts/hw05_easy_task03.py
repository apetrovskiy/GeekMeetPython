__author__ = 'Петровский А.Е.'

import os

root_path = os.getcwd();
print(__file__)
result_file_path = __file__ + "_copy.py"
print(result_file_path)

with open(__file__, 'r', encoding='UTF-8') as f:
    file_content = f.readlines()
    with open(result_file_path, 'w', encoding='UTF-8') as f2:
        f2.write("".join(file_content))

with open(result_file_path, 'r', encoding='UTF-8') as f3:
    print(f3.readlines())
