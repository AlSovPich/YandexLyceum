word1 = str(input())
word1 = list(word1)
word2 = str(input())
word2 = list(word2)
if word2[0] == word1[-1]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
