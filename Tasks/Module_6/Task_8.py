string_of_letters = input()
list_of_letters_1 = list(string_of_letters)

print(list_of_letters_1[2])

print(list_of_letters_1[-1])

print("".join(map(str, list_of_letters_1[:5])))

print("".join(map(str, list_of_letters_1[0:-2])))

list_of_letters_2 = []
list_of_letters_3 = []
for i in range(0, len(list_of_letters_1)):
    if i % 2 == 0:
        list_of_letters_2.append(list_of_letters_1[i])
    elif i % 2 == 1:
        list_of_letters_3.append(list_of_letters_1[i])
print("".join(map(str, list_of_letters_2)))
print("".join(map(str, list_of_letters_3)))

list_of_letters_1.reverse()
print("".join(map(str, list_of_letters_1)))

list_of_letters_4 = []
for i in range(0, len(list_of_letters_1)):
    if i % 2 == 0:
        list_of_letters_4.append(list_of_letters_1[i])
print("".join(map(str, list_of_letters_4)))
