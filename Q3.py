import math

n = 600851475143
d = 2

def isprime(n):
    a = False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            a = True
            return False
            break
    if a == False:
        return True


while True:
    if n % d == 0:
        print(d)

        if isprime(int(n/d)) == True:
            print(int(n/d))
            break


    d += 1
