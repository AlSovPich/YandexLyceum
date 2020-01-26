inp = '\n'
new = input()
for i in range(int(new[1:-1])):
    new = input()
    if new[1] != '#' and new != '':
        inp += new + '\n'
print(inp)
