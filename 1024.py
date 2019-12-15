num = int(input())
stepen = 0
while num // 2 > 0:
    num = num / 2
    stepen += 1
if num != 1:
    print('НЕТ')
else:
    print(stepen)
