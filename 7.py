temperature = float(input())
print(temperature)
if temperature < 15.5:
    print('ХОЛОДНО')
if temperature > 28:
    print('ЖАРКО')
if temperature <= 28 and temperature >= 15.5:
    print('НОРМАЛЬНО')
