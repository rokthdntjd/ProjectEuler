n = 1
An = 0

def divisor_count(num):
    global a
    a = 0
    for i in range(1, num):
        if num % i == 0:
            a += 1
    return a

while True:

    An += n

    divisor_count(An)

    if a > 500:
        print(An, n, a)
        print(list)
        break
    print(An, n, a)
    n += 1









'''
import math

a = 12800
c = 0
max = 0
maxn = 0
maxa = 0

while True:
    c = 0
    n = 0
    for i in range(0, a+1):
        n += int(i)
    for i in range(1, n+1):
        if n%i == 0:
            c += 1

    if int(c) > max:
        max = int(c)
        maxn = n
        maxa = a

    if int(c) > 500:
        print("------------------------------")
        print(a ,"|", n ,"|", c ,"|", max)
        break

    print(a ,"|", n ,"|", c ,"|", max ,"|", maxa ,"|", maxn)
    a += 1
'''
