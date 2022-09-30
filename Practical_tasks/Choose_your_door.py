import random

selected_door_0 = 0
selected_door_1 = 0
total = 100000

while total != 0:
    a = [0, 1, 0]
    c = random.choice(a)
    print(c)
    a = [0, 1]
    if c == 0:
        selected_door_1 += 1
    elif c == 1:
        selected_door_0 += 1
    total -= 1

print("Если изменить выбор при оставшихся двух дверях с изначально выбранной на оставшуюся, шанс на победу составит: ", selected_door_1 / 1000, "%" " а шанс на порожение составит: ", selected_door_0 / 1000, "%", sep = '')