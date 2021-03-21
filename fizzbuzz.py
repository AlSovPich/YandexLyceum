a = int(input())
b = int(input())
for i in range(a, b + 1):
    if 0 == i % 3 and 0 == i % 5:
        print('FizzBuzz')
        continue
    if 0 == i % 3:
        print('Fizz')
        continue
    if 0 == i % 5:
        print('Buzz')
        continue
    print(i)
            
        
