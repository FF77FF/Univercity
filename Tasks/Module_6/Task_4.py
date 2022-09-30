list_of_numbers_1 = [int(s) for s in input().split()]
max = -10000000
min = 10000000
for i in range(0, len(list_of_numbers_1)):
    if list_of_numbers_1[i] > max:
        max = list_of_numbers_1[i]
    elif list_of_numbers_1[i] < min:
        min = list_of_numbers_1[i]
index_of_max_num = list_of_numbers_1.index(max)
index_of_min_num = list_of_numbers_1.index(min)
list_of_numbers_1[index_of_min_num], list_of_numbers_1[index_of_max_num] = list_of_numbers_1[index_of_max_num], list_of_numbers_1[index_of_min_num]
print(" ".join(map(str, list_of_numbers_1)))