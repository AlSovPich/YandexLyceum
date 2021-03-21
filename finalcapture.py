n = int(input())
if 0 > n:
    print('Пуск')
    exit(0)
print('Осталось секунд: ' + str(n))
for i in range(n):
    n -= 1
    print('Осталось секунд: ' + str(n))
if 0 == n:
    print('Пуск')
