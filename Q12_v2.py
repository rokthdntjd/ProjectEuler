import math

for i in range(0, 10):
    prev_num = 1
    n = 0
    
    curr_num = prev_num + n

    n = n + 1
    prev_num = curr_num
    
    print(curr_num, prev_num, n)

