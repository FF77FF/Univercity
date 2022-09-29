a = int(input())
if (int(a / 1000) == a % 10) and (int(a % 1000 / 100) == int(a % 100 / 10)):
    print("Да")
else:
    print("Нет")