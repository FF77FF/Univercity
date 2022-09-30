list_of_numbers = [int(s) for s in input().split()]
i = 1
while i < len(list_of_numbers):
    list_of_numbers[i - 1], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[i - 1]
    i += 2
print(" ".join(map(str, list_of_numbers)))