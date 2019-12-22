text = ''
num = 1
times = 0
while not("СТОП" in text):
    newtext = str(input())
    text += newtext
    if not("кот" in text or "Кот" in text):
        num += 1
    if ("кот" in newtext or "Кот" in newtext):
        times += 1
if times == 0:
    print(str(times) + ' ' + '-1')
else:
    print(str(times) + ' ' + str(num))
