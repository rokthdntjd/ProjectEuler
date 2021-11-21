import math

def tri_num(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a

def ifsquare(n):
    a = 1
    while True:
        if a^2 == n:
            return True
            break
        a += 1

print(ifsquare(10))