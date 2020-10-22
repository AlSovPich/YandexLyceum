import sys
gematrs = []
words = []
change = 0
for line in sys.stdin:
    summ = 0
    words.append(line)
    line = line.upper()
    for i in range(len(line)):
        code = ord(line[i]) - ord('A') + 1
        summ += code
    gematrs.append(summ)
for j in range(1, len(words)):
    if gematrs[j - 1] > gematrs[j]:
        change = gematrs[j]
        gematrs[j] = gematrs[j - 1]
        gematrs[j - 1] = change
        change = words[j - 1]
        words[j - 1] = words[j]
        words[j] = change
    if gematrs[j - 1] == gematrs[j]:
        if ord(words[j - 1][0]) > ord(words[j][0]):
            change = gematrs[j]
            gematrs[j] = gematrs[j - 1]
            gematrs[j - 1] = change
            change = words[j - 1]
            words[j - 1] = words[j]
            words[j] = change
print(words)