best_count = 0
count = 0
best_i = 0

for i in range (1,1000001):
    print(i)
    temp_i = i
    count = 0
    while i != 1:
        if i%2 == 0:
            i = i/2
            count += 1
        else:
            i = 3*i+1
            count += 1
    if count > best_count:
        best_count = count
        best_i = temp_i

print(best_count)
print(best_i)
