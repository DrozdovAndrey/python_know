import os

# file_path = "C:/Users/User/Documents/example.txt"


import os
def get_file_info(file_path: str) -> tuple:
    *path, filename = file_path.split('/')
    *name, extension = filename.split('.')
    return '/'.join(path), '.'.join(name), '.' + extension


def get_file_info2(file_path: str) -> tuple:
    path, filename = os.path.split(file_path,)
    *name, extension = filename.split('.')
    if path != '':
        path += '/'
    return path, '.'.join(name), '.' + extension


def get_file_info3(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


print(get_file_info(file_path = 'file_in_current_directory.txt'))

print(get_file_info2(file_path = 'C:/Users/User/Documents/example.txt'))