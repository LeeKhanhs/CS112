def count_ways_to_withdraw_money(n, S, denominations):
    def withdrawMoney(id, total, path):
        if total == S:
            ways.append(path)  
            return
        for i in range(id, n):
            if denominations[i] + total <= S:
                withdrawMoney(i, total + denominations[i], path + [denominations[i]])

    ways = []  

    withdrawMoney(0, 0, [])

    return ways

n, S = map(int, input().split())
denominations = list(map(int, input().split()))
denominations.sort()  

ways = count_ways_to_withdraw_money(n, S, denominations)

print(len(ways))  

for way in ways:
    print(' '.join(map(str, way)))  