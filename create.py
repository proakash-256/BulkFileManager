import os


def create(path, num, name, start=1):
    i = start
    for _ in range(num):
        os.mkdir(f"{path}/{name}{i}")
        i += 1