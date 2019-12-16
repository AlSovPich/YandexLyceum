M = int(input())
N = int(input())
shelf = set()
for i in range(M):
    shelf.add(str(input()))
for n in range(N):
    book = str(input())
    if book in shelf:
        print('YES')
    else:
        print('NO')
        
    
    
    
