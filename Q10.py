import math

list = []

for i in range(2, 2000001):
    print(i)
    c = False

    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            c = True

    if c == False:
        list.append(int(i))

print(sum(list))
