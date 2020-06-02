endurance = int(input())
mistakes = 0
right = 0
while mistakes < endurance:
    text = str(input())
    if right % 4 == 0 and not('раз' == text):
        mistakes += 1
        print('Правильных отсчётов было ' + str(right) + ', но теперь вы ошиблись.')
        right = 0
        continue
    if right % 4 == 1 and not('два' == text):
        mistakes += 1
        print('Правильных отсчётов было ' + str(right) + ', но теперь вы ошиблись.')
        right = 0
        continue
    if right % 4 == 2 and not('три' == text):
        mistakes += 1
        print('Правильных отсчётов было ' + str(right) + ', но теперь вы ошиблись.')
        right = 0
        continue
    if right % 4 == 3 and not('четыре' == text):
        mistakes += 1
        print('Правильных отсчётов было ' + str(right) + ', но теперь вы ошиблись.')
        right = 0
        continue
    right += 1
    
print('На сегодня хватит.')
