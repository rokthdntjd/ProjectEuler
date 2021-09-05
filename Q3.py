import math

list = []

for i in range(2, 600851475143):
    n = 600851475143
    print(n)
    if n%i == 0:
        n = n/i
        list.append(i)
print(list)
