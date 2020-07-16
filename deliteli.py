number = int(input())
first = ('')
num = 0
for i in range(1, number + 1):
    if (0 == (number % i)):
        first += (str(i) + ' ')
        num += 1
print(first)
if num > 2 or 1 == num:
    print('НЕТ')
else:
    print('ПРОСТОЕ')
        
