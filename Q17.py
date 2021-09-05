list = []

for i in range(1, 1001):
    print(i)

    #1자리
    if len(str(i)) == 1:
        if int(i) == 1 or int(i) == 2 or int(i) == 6:
            list.append(int(3))
        if int(i) == 4 or int(i) == 5 or int(i) == 9:
            list.append(int(4))
        if int(i) == 3 or int(i) == 7 or int(i) == 8:
            list.append(int(5))

    #2자리
    if len(str(i)) == 2:
        if int(i) == 10:
            list.append(int(3))
        if int(i) == 11 or int(i) == 12  or int(i) == 20:
            list.append(int(6))
        if int(i) == 15 or int(i) == 16:
            list.append(int(7))
        if int(i) == 13 or int(i) == 14 or int(i) == 18 or int(i) == 19:
            list.append(int(8))
        if int(i) == 17:
            list.append(int(9))

        if str(i)[0] == 4 or str(i)[0] == 5 or str(i)[0] == 6:
            list.append(int(5))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))

        if int(str(i)[0]) == 2 or int(str(i)[0]) == 3 or int(str(i)[0]) == 8 or int(str(i)[0]) == 9:
            list.append(int(6))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))

        if int(str(i)[0]) == 7:
            list.append(int(7))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))


    #3자리
    if len(str(i)) == 3:
        list.append(int(3))
        if int(str(i)[0]) == 1 or int(str(i)[0]) == 2 or int(str(i)[0]) == 6:
            list.append(10)
        if int(str(i)[0]) == 4 or int(str(i)[0]) == 5 or int(str(i)[0]) == 9:
            list.append(11)
        if int(str(i)[0]) == 3 or int(str(i)[0]) == 7 or int(str(i)[0]) == 8:
            list.append(12)

        if int(str(i)[1:]) == 10:
            list.append(int(3))
        if int(str(i)[1:]) == 11 or int(str(i)[1:]) == 12  or int(str(i)[1:]) == 20:
            list.append(int(6))
        if int(str(i)[1:]) == 15 or int(str(i)[1:]) == 16:
            list.append(int(7))
        if int(str(i)[1:]) == 13 or int(str(i)[1:]) == 14 or int(str(i)[1:]) == 18 or int(str(i)[1:]) == 19:
            list.append(int(8))
        if int(str(i)[1:]) == 17:
            list.append(int(9))

        if str(i)[1] == 4 or str(i)[1] == 5 or str(i)[1] == 6:
            list.append(int(5))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))
forgot to add the 0 cases :(
        if int(str(i)[1]) == 2 or int(str(i)[1]) == 3 or int(str(i)[1]) == 8 or int(str(i)[1]) == 9:
            list.append(int(6))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))

        if int(str(i)[1]) == 7:
            list.append(int(7))
            if int(str(i)[-1]) == 1 or int(str(i)[-1]) == 2  or int(str(i)[-1]) == 6:
                list.append(int(3))
            if int(str(i)[-1]) == 4 or int(str(i)[-1]) == 5  or int(str(i)[-1]) == 9:
                list.append(int(4))
            if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7  or int(str(i)[-1]) == 8:
                list.append(int(5))



    #4자리
    if len(str(i)) == 4:
        list.append(int(11))

print(sum(list))
