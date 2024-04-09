# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files



with open('__init__.py', 'w', encoding='utf-8') as f:
    f.writelines('import os\n')
    f.writelines('def rename_files(desired_name, num_digits, source_ext, target_ext, range_str=None):\n')
    f.writelines('    os.chdir("test_folder")\n')
    f.writelines('    lst = os.listdir()\n')
    f.writelines('    count = 1\n')
    f.writelines('    for i in lst:\n')
    f.writelines("        *_, b = i.split('.')\n")
    f.writelines('        if b == source_ext:\n')
    f.writelines('            if range_str:\n')
    f.writelines("                new_name = f'{i[range_str[0]:range_str[1]]}{desired_name}{count:0{num_digits}}.{target_ext}'\n")
    f.writelines('            else:\n')
    f.writelines("                new_name = f'{desired_name}{count:0{num_digits}}.{target_ext}'\n")
    f.writelines('            os.rename(i, new_name)\n')
    f.writelines('            count += 1\n')

# решение из задачи
code_to_write = '''
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    files = os.listdir('geekbrains')

    filtered_files = [file for file in files if file.endswith(source_ext)]

    filtered_files.sort()

    num = 1

    for file in filtered_files:
        name = os.path.splitext(file)[0]

        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        os.rename(file, new_name)

        new_names.append(new_name)

        num += 1

    return new_names
'''

with open("__init1__.py", "w") as init_file:
    init_file.write(code_to_write)
