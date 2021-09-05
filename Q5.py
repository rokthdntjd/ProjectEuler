n = 20

while True:
    c = False
    print(n)
    for i in range(1, 21):
        if n%i != 0:
            c = True
    if c == False:
        print(n)
        break
    n += 1
