answer = 0

for i in range(100, 1000):
    for j in  range(100, 1000):

        num = i*j
        print(i, j, num)
        num_reversed = str(num)[::-1]
#        print(num_reversed)

        if int(num) == int(num_reversed):
            if int(num) > answer:
                answer = num

print(answer)
