cost = float(input())
all_cost = 0
while cost >= 0:
    if cost > 1000:
        cost = cost * 0.95
    all_cost = all_cost + cost 
    cost = float(input())
print(all_cost)
