list_of_numbers_1 = [int(s) for s in input().split()]
list_of_numbers_2 = []
for i in range(1, len(list_of_numbers_1)):
    if list_of_numbers_1[i - 1] < list_of_numbers_1[i]:
        list_of_numbers_2.append(list_of_numbers_1[i])
print(" ".join(map(str, list_of_numbers_2)))