import math
string_or_letters = input()
list_of_letters_1 = list(string_or_letters)
k = float(len(list_of_letters_1)) / 2
max = math.ceil(k)
list_of_letters_2 = list_of_letters_1[max: len(list_of_letters_1)] + list_of_letters_1[0: max]
print("".join(map(str, list_of_letters_2)))
