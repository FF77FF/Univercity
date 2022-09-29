N = int(input())
i = 1
while i ** 2 <= N:
    print(i ** 2)
    i += 1
    if i ** 2 > N:
        break
