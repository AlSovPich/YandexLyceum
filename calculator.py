num1 = float(input())
num2 = float(input())
op = input()
if '+' == op:
    print(num1 + num2)
else:
    if '-' == op:
        print(num1 - num2)
    else:
        if '*' == op:
            print(num1 * num2)
        else:
            if '/' == op:
                if 0 == num2:
                    print('888888')
                else:
                    print(num1 / num2)
            else:
                print('888888')
