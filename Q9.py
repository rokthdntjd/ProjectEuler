# a+b+c = 1000
# a= 1000-b-c, b= 1000-a-c, c=  1000-a-b

for i in range(0, 1001):
    for j in range(0, 1001-int(i)):
        k = 1000-int(i)-int(j)
        if i**2 + j**2 == k**2:
            print(i*j*k)
