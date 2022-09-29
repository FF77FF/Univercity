N = int(input())
k = 0
a, b = 0, 1
while N > k:
    a, b = b, a + b
    k += 1
    if k == N:
        print(a)
