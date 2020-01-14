word1 = str(input())
word2 = str(input())
while list(word2)[0] == list(word1)[-1]:
    word1 = word2
    word2 = str(input())
print(word2)
