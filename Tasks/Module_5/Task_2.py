x = int(input())
n = 1
while x >= (2 ** n):
    if 2 ** (n + 1) > x:
        print(n, 2 ** n)
        break
    else:
        n += 1