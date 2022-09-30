list_of_numbers = [int(s) for s in input().split()]
for i in range(0, len(list_of_numbers)):
    if i == list_of_numbers.index(list_of_numbers[i]):
        print("НЕТ")
    else:
        print("ДА")
