def how_many_ways(m, coins):
    memo = {}
    
    memo[0] = 1

    for i in range(1, m + 1):
        memo[i] = 0
        
        for coin in coins:
            subproblem = i - coin
            
            if subproblem < 0:
                continue

            if i not in memo:
                memo[i] = 0

            memo[i] += memo[subproblem]

    return memo[m]
K = int(input())
coins = list(map(int, input().split()))
Target = int(input())

print(how_many_ways(Target, coins))