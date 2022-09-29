a = int(input())
b = int(input())
c = int(input())

def number_of_tables(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(n / 2 + 1)

print(int(number_of_tables(a) + number_of_tables(b) + number_of_tables(c)))