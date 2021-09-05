n = "08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748"

list = [[] for i in range(20)]
print(list)
#list[2].append(1)

a = 0

while a < 20:
    for i in range(1, 401):
        if int(i) % 20 == 0:
            list[int(a)].append(str(n[2*i - 2:2*i]))
            a += 1
        else:
            list[int(a)].append(str(n[2*i - 2:2*i]))

print(list)


#가로
hori_sum = 0
hori_gongbackcount = 0

for i in range(0, 20):
    for j in range(0, 20):
        if int(j) == 17 or int(j) == 18 or int(j) == 19:
            hori_gongbackcount += 1
        else:
            n1 = list[i][j]
            n2 = list[i][j+1]
            n3 = list[i][j+2]
            n4 = list[i][j+3]
            temp_hori_sum = int(n1) * int(n2) * int(n3) * int(n4)
            if temp_hori_sum > hori_sum:
                hori_sum = temp_hori_sum

print(hori_sum)
print(hori_gongbackcount)
print("horizontal calculations done :)")


#세로
verti_sum = 0
verti_gongbackcount = 0

for i in range(0, 20):
    for j in range(0, 20):
        if int(i) == 17 or int(i) == 18 or int(i) == 19:
            verti_gongbackcount += 1
        else:
            n1 = list[i][j]
            n2 = list[i+1][j]
            n3 = list[i+2][j]
            n4 = list[i+3][j]
            temp_verti_sum = int(n1) * int(n2) * int(n3) * int(n4)
            if temp_verti_sum > verti_sum:
                verti_sum = temp_verti_sum

print(verti_sum)
print(verti_gongbackcount)
print("vertical calculations done :)")


#대각선 1 (왼위 - 오아래)
diag1_sum = 0
diag1_gongbackcount = 0

for i in range(0, 20):
    for j in range(0, 20):
        if int(j) == 17 or int(j) == 18 or int(j) == 19 or int(i) == 17 or int(i) == 18 or int(i) == 19:
            diag1_gongbackcount += 1

        else:
            n1 = list[i][j]
            n2 = list[i+1][j+1]
            n3 = list[i+2][j+2]
            n4 = list[i+3][j+3]
            print(i, j, n1, n2, n3, n4)
            temp_diag1_sum = int(n1) * int(n2) * int(n3) * int(n4)
            if temp_diag1_sum > diag1_sum:
                diag1_sum = temp_diag1_sum

print(diag1_sum)
print(diag1_gongbackcount)
print("diagonal 1 calculations done :)")


#대각선 2 (왼아래 - 오위)
diag2_sum = 0
diag2_gongbackcount = 0

for i in range(0, 20):
    for j in range(0, 20):
        if int(j) == 0 or int(j) == 1 or int(j) == 2 or int(i) == 17 or int(i) == 18 or int(i) == 19:
            diag2_gongbackcount += 1

        else:
            n1 = list[i][j]
            n2 = list[i+1][j-1]
            n3 = list[i+2][j-2]
            n4 = list[i+3][j-3]
            print(i, j, n1, n2, n3, n4)
            temp_diag2_sum = int(n1) * int(n2) * int(n3) * int(n4)
            if temp_diag2_sum > diag2_sum:
                diag2_sum = temp_diag2_sum

print(diag2_sum)
print(diag2_gongbackcount)
print("diagonal 2 calculations done :)")

list_sum = [hori_sum, verti_sum, diag1_sum, diag2_sum]
print(max(list_sum))
