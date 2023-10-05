import os
import extention


def rename(path, name, start=1):
    i = start
    for file_name in os.listdir(path):
        old_name = path + file_name
        ex = extention.get(file_name)
        new_name = path + name + str(i) + ex
        os.rename(old_name, new_name)
        i += 1
