size = input()
min = 10000000000
max = 0
number = 0
while size != '!':
    if int(size) <= 190 and int(size) >= 150:
        number += 1
        if min > int(size):
            min = int(size)
        if max < int(size):
            max = int(size)
    size = input()
print(number)
print(str(min) + ' ' + str(max))
        
