text = str(input())
num = 1
if "кот" in text or "Кот" in text:
    print(1)
    exit(0)
while not("СТОП" in text or "кот" in text or "Кот" in text):
    num += 1
    text += str(input())
if not("кот" in text or "Кот" in text):
    print(-1)
else:
    print(num)
