text = str(input())
num = 0
if "кот" in text or "Кот" in text:
    print(1)
    exit(0)
while not("СТОП" in text):
    while not("кот" in text or "Кот" in text):
        num += 1
    text += str(input())
if not("кот" in text or "Кот" in text):
    print(-1)
else:
    print(num)

