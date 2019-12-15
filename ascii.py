high = int(input())
len = int(input())
sym = str(input())
for i in range(1, high + 1):
    if i == 1 or i == high:
        print(sym * len)
    else:
        print(sym + (' ' * (len - 2)) + sym) 
        
