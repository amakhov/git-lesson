list = [1, 2, 3, 8, 14, 89, 45]
n = 0
i = 0
i2 = len(list) - 1
r = 0
for x in list:
    r += 1
    if r <= (len(list)//2):
        list[i] = list[i2]
        list[i2] = x
        i += 1
        i2 -= 1
    else:
        break
print(list)
