code = input()
if code[1] != code[2]:
    if code[1] != code[3]:
        if code[3] != code[2]:
            print('ОК')
if code[1] == code[2]:
    if code[1] == code[3]:
        if code[3] == code[2]:
            print('В числе все цифры одинаковые')
if code[1] == code[2] or code[1] == code[3] or code [2] == code[3]:
    if not(code[1] == code[2]) or not(code[1] == code[3]) or not(code [2] == code[3]):
        print('В числе две одинаковые цифры')
