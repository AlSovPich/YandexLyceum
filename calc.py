import math
op = ''
while 'x' != op:
    answer = 0
    num1 = int(input())
    op = str(input())
    if '+' == op:
        answer = num1 + int(input())
        print(answer)
        continue
    if '-' == op:
        answer = num1 - int(input())
        print(answer)
        continue
    if '*' == op:
        answer = num1 * int(input())
        print(answer)
        continue
    if '%' == op:
        answer = num1 % int(input())
        print(answer)
        continue
    if '!' == op:
        answer = 1
        if num1 >= 0:
            for i in range(1, num1 + 1):
                answer *= i
        else:
            answer = 0
        print(answer)
        continue
    if '/' == op:
        answer = math.floor(num1 / int(input()))
        print(answer)
        continue
print(num1)
        
    
