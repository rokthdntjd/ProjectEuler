import math

n = int(input("number: "))
a = False
list = []
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        a = True
        list.append(i)
if a == True:
    print("is not prime")
    print(list)
if a == False:
    print("is prime")
    print(list)
