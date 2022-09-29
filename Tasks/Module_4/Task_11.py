a = int(input())
b = int(input())
x = int(input())
y = int(input())

def Сolor(n, m):
    if (n == m) or (n == m + 2) or (m == n + 2) or (n == m + 4) or (m == n + 4) or (n == m + 6) or (m == n + 61):
        return "Черная"
    else:
        return "Белая"

if Сolor(a, b) == Сolor(x, y):
    print("Да")
else:
    print("Нет")
