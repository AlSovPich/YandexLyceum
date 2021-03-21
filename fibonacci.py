num = 1
prev_num = num
max = int(input())
print(num)
print(prev_num)
while num < max:
    next_num = prev_num + num
    prev_num = num
    num = next_num
    if num < max:
        print(num)
    
