import os


def rename(path):
    i = 0
    for file_name in os.listdir(path):
        new_name = path + "Image" + str(i) + ".jpg"
        old_name = path + file_name
        os.rename(old_name, new_name)
        i += 1


if __name__ == "__main__":
    path = input("Enter the path of the folder: ")
    rename(path)
