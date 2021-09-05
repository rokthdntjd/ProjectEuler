import math

list = []
n = 2

while True:
    c = False
    print(n)

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            c = True

    if c == False:
        list.append(n)

    if int(len(list)) >= 10001:
        print(list[10000])
        break

    n += 1
