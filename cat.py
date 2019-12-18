num = int(input())
text = ''
for i in range(1, num + 1):
    text += str(input())
if "кот" in text or "Кот" in text:
    print('МЯУ')
else:
    print('НЕТ')
