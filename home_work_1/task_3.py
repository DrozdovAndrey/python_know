list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

count_numbers = 0
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            count_numbers += 1
print(count_numbers)
