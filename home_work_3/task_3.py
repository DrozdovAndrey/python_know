lst = [1, 2, 3]

# Введите ваше решение ниже
list2 = []
for i in lst:
    if i not in list2:
        if lst.count(i) > 1:
            list2.append(i)
print(list2)
