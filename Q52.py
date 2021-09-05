'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

num1 = input()
num2 = input()

num1_list = []
num2_list = []

for i in str(num1):
    num1_list.append(i)
for j in str(num2):
    num2_list.append(j)

print(num1_list.sort())
print(num2_list)

num1_list_sorted = num1_list.sort()
num2_list_sorted = num2_list.sort()

print(num1_list_sorted)
print(num2_list_sorted)

if len(num1_list) > len(num2_list):
    for i in range(0, int(len(num1_list_sorted))):
        if num1_list_sorted[i] != num2_list_sorted[i]:
            print("naaaaaaa")
            break
        else:
            print("yeeeeeee")
