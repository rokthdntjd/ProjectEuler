sumlist = []
squarelist = []


for i in range(1, 101):
    sumlist.append(int(i)**2)
    squarelist.append(i)

print(int(sum(squarelist)))
print(sum(sumlist))
