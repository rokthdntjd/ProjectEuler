list2 = []
list = []

for i in range(1, 1000):
    if i % 3 == 0:
        list.append(i)
    if i % 5 == 0:
        list.append(i)
for i in range(1, 1000):
    if i % 15 == 0:
        list2.append(i)

print(sum(list) - sum(list2))

print("this was changed")
