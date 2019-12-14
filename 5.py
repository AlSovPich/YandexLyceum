d = float(input()) #day
m = float(input()) #month
y = float(input()) #year
a = (d + ((13 * m - 1) // 5 ) + y + (y // 4 + 20 // 4 - 2 * 20 + 777))
b = (round(d + ((13 * m - 1) // 5 ) + y + (y // 4 + 20 // 4 - 2 * 20 + 777) // 7) * 7)
l = a - b
print (l - 1)
     
