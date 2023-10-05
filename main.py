from create import create
from rename import rename

if __name__ == "__main__":
    print("Enter 1 to Create Bulk Folders")
    print("Enter 2 to Rename Bulk Folders/Files")
    ch = int(input("Enter your choice: "))

    path = input("Enter the path of the directory: ")
    if path[-1] != "\\":
        path += "\\"

    if ch == 1:
        num = int(input("Enter the number of folders: "))
        name = input("Enter the name of the folder: ")
        start = input("Enter the start value: ")
        if start == "":
            create(path, num, name)
        else:
            create(path, num, name, int(start))
        print("Folders created successfully!!")

    if ch == 2:
        name = input("Enter the name of the folder/file: ")
        start = input("Enter the start value: ")
        if start == "":
            rename(path, name)
        else:
            rename(path, name, int(start))
        print("Folder Contents renamed successfully!!")
