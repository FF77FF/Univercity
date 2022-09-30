list_of_numbers_1 = [int(s) for s in input().split()]
list_of_numbers_2 = [int(p) for p in input().split()]
list_of_numbers_3 = []
for i in range(0, len(list_of_numbers_1)):
    for j in range(0, len(list_of_numbers_2)):
        if list_of_numbers_1[i] == list_of_numbers_2[j]:
            list_of_numbers_3.append(list_of_numbers_2[j])
print(" ".join(map(str, list_of_numbers_3)))