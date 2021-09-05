'''
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''




b = 1
max_digit_sum = 0
temp_digit_sum = 0
temp_list = []
for a in range (1, 101):
    b = 1
    print(a, b)
    while b<=100:
        temp_list = []
        for i in str(a ** b):
            temp_list.append(int(i))
        temp_digit_sum = sum(temp_list)
        if temp_digit_sum > max_digit_sum:
            max_digit_sum = temp_digit_sum
        b+=1


print(max_digit_sum)
