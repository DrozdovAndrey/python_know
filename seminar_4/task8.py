# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

num, tasks, s = 1, 2, 3

def change_val():
    '''работа с именами переменных'''
    x = 10
    my_var_name = [k for k in globals().keys() if not k.startswith('__')]
    print("Список без магических имен ", my_var_name, sep='\n')
    for i in my_var_name:
        if i[-1] =='s' and len(i) != 1:
            globals()[i[:-1]] = globals()[i]
            globals()[i] = None
    my_var_name_1 = [k for k in globals().keys() if not k.startswith('__')]
    print(locals().items())
    print(my_var_name_1)
    print(globals())


change_val()
print(tasks, task)