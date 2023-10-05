def get(name):
    dot_index = name.find('.')
    if dot_index == -1:
        return ""
    return name[dot_index:]
