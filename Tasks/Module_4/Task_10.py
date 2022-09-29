a = int(input())
b = int(input())
if (a == b) or (a == b + 2) or (b == a + 2) or (a == b + 4) or (b == a + 4) or (a == b + 6) or (b == a + 61):
    print("Черная")
else:
    print("Белая")
