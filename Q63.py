n = 2
c = 0


while True:
    print(str(int(n)**int(n)))
    if len(str(int(n)**int(n))) == int(n):
        print(n)
    n += 1


print(c)
