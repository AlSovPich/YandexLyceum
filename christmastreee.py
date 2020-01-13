N = int(input())
st = 0
stnum = 1
allnum = 1
while allnum <= N:
    print(allnum, end=' ')
    allnum += 1
    st += 1
    if st == stnum:
        print()
        stnum += 1
        st = 0
        
    
