num = int(input())
before = set()
for i in range(num):
    city = str(input())
    before.add(city)
new = str(input())
if new in before:
    print('TRY ANOTHER')
else:
    print('OK')
    
