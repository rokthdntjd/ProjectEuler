n = int(286)

while True:

    t = float((n*(n+1))/2)
    for i in range(1, n):
        print(n, t, i, float((i*(3*n - 1))/2))
        if float((i*(3*n - 1))/2) == float(t):
            print(t)
            for j in range(1, n):
                if float(j*(2*j-1)) == float(t):
                    print(n, t, i, j)
                    break

    n += 1
