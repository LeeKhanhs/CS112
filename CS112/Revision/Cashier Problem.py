def minimum_coins(coins, target):
    INF = float('inf')
    dp = [INF] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != INF else -1

k = int(input())
coins = list(map(int, input().split()))
target = int(input())

result = minimum_coins(coins, target)

print(result)