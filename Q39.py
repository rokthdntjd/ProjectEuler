'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

max_n = 0
max_h = 0
list_n = []
list_h = []

for h in range(1, 1001):
    n = 0
    for i in range(1, int(h)+1):
        for j in range(1, int(h)-int(i)+1):
            k = int(h) - int(i) - int(j)
            if i**2 + j**2 == k**2:
                print(i, j, k, h)
                n += 1

    list_n.append(n)
    list_h.append(h)

print(list_n)
print(max(list_n))
print(list_h[list_n.index(max(list_n))])
