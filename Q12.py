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

an = 1

while True:
    divisor_count = 0

    if ifsquare(tri_num(an)) == True:
        divisor_count += 1

    a = 0
    for i in range(1, tri_num(an)):
        if tri_num(an) % i == 0:
            if i >= tri_num(an)/i:
                divisor_count += a*2
                break
            