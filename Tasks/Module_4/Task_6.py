a = int(input())
if (a / 100 < a % 100 / 10) and (a % 100 / 10 < a % 10):
    print("Да")
else:
    print("Нет")
