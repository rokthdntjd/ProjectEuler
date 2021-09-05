a = 0

for i in range (2, 10001):
    print(i)
    n = 0
    c = False
    while n <= 50:
        print(i, str(i)[::-1])
        b = int(i) + int(str(i)[::-1])
        if str(b) == str(b)[::-1]:
            c = True
            print("---------------------------------------------------------")
            break
        else:
            i = int(i) + int(str(i)[::-1])
            n += 1
    if c == False:
        a += 1
print(a)
