N = int(input())
k = 1
a, b = 0, 1
while N >= k:
    a, b = b, a + b
    k += 1
    if N == b:
        print(k)
        break
    elif N < b:
        print("-1")
