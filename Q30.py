sumlist = []

for i in range(2, 10000000000):
    list = []
    for j in str(i):
        list.append(int(j)**5)
    if sum(list) == int(i):
        print(i)
        print(list)
        sumlist.append(int(i))
        print(sum(sumlist))
