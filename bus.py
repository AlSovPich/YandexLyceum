num = str(input())
first = set()
second = set()
third = set()
while num != '':
    first.add(num)
    num = str(input())
num = str(input())
while num != '':
    second.add(num)
    num = str(input())
for i in first:
    if i in second:
        third.add(i)
if third != {}:
    for n in third:
        print(n)
if third == set():
    print('EMPTY')
    
    
    
