a, b = 1, 2
list = []

while a < 4000000:
    print(a)

    if a%2 == 0:
        list.append(int(a))

    c = b
    b = a + b
    a = c

print(sum(list))
