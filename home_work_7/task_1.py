# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
# Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
import os


def rename_files(desired_name, num_digits, source_ext, target_ext, range_str=None):
    os.chdir('test_folder')
    lst = os.listdir()
    count = 1
    for i in lst:
        *_, b = i.split('.')
        if b == source_ext:
            if range_str:
                new_name = f'{i[range_str[0]:range_str[1]]}{desired_name}{count:0{num_digits}}.{target_ext}'
                os.rename(i, new_name)
                count += 1
            else:
                new_name = f'{desired_name}{count:0{num_digits}}.{target_ext}'
                os.rename(i, new_name)
                count += 1

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, 1.txt, new_file_006.doc, new_file_003.doc, 2.txt, new_file_009.doc, new_file_010.doc

# решение из задачи
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#
#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#
#     # Сортируем файлы по имени
#     filtered_files.sort()
#
#     # Задаем начальный номер для порядкового номера
#     num = 1
#
#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]
#
#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#
#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#
#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#
#         # Увеличиваем порядковый номер
#         num += 1
#
