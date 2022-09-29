month = int(input())
day = int(input())
if month == 2 and day == 28:
    print("1", month + 1, "2022", sep = "-")
elif (month == 4 or month == 6 or month == 9 or month == 11) and (day == 30):
    print("1", month + 1, "2022", sep = "-")
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day == 31):
    print("1", month + 1, "2022", sep = "-")
else:
    print(day + 1, month, "2022", sep = "-")
