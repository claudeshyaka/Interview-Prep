def whatFlavors(cost, money):
    # Write your code here
    d = {}
    x, y = 0, 0
    
    for i in range(1, len(cost) + 1):
        temp = money - cost[i-1]
        if temp in d:
            x, y = temp, cost[i-1]
            break
        d[cost[i-1]] = i
        
    r = [i+1 for i, c in enumerate(cost) if c == x or c == y]
    print(min(r), max(r))


money = 5
cost = [2, 1, 3, 5, 6]
whatFlavors(cost, money)