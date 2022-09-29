a = int(input())
b = int(input())
k = 1
max = 1
while b != 0:
    if a == b:
        k += 1
    elif a != b and max < k:
        max = k
        k = 1
    a = b
    b = int(input())
print(max)