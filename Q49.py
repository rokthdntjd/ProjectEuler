'''
1487, 4817, 8147은 3330씩 늘어나는 등차수열입니다. 이 수열에는 특이한 점이 두 가지 있습니다.

세 수는 모두 소수입니다.
세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.
1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위엣것 말고도 또 다른 수열이 존재합니다.

그 수열의 세 항을 이었을 때 만들어지는 12자리 수는 무엇입니까?

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

list_i = []
list_j = []
list_k = []

n1 = False
n2 = False
n3 = False

list_a = []
list_b = []
list_c = []

n = []

for i in range(1000, 10000-6660):

    list_i = []
    list_j = []
    list_k = []

    j = i + 3330
    k = j + 3330
    print(i, j, k)
    for a in str(i):
        list_i.append(a)
    for a in str(j):
        list_j.append(a)
    for a in str(k):
        list_k.append(a)

    print(list_i)
    print(list_j)
    print(list_j)

    list_i.sort()
    list_j.sort()
    list_k.sort()

    if list_i == list_j and list_j == list_k and list_k == list_i:

        n1 = False
        n2 = False
        n3 = False

        list_a = []
        list_b = []
        list_c = []

        for a in range(2, int(i)):
            if i%a == 0:
                list_a.append(a)
        if len(list_a) == 0:
            n1 = True

        for a in range(2, int(j)):
            if j%a == 0:
                list_b.append(a)
        if len(list_b) == 0:
            n2 = True

        for a in range(2, int(k)):
            if k%a == 0:
                list_c.append(a)
        if len(list_c) == 0:
            n3 = True

        if n1 == True and n2 == True and n3 == True:
            print(i,j,k)
            n.append(i)
            n.append(j)
            n.append(k)

print(n)
