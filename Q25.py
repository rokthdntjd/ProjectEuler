a = 0
b = 1
count = 2

while True:
    temp = a
    a = b
    b = temp + b
    print(a)
    print(b)
    count += 1
    if len(str(a))>=1000:
        print(count-3)
        break
