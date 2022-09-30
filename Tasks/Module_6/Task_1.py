list_of_numbers_1 = [int(s) for s in input().split()]
list_of_numbers_2 = [int(s) for s in list_of_numbers_1 if s % 2 == 1]
print(" ".join(map(str, list_of_numbers_2)))

