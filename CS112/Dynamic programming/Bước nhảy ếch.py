def can_cross_river(n, stones):
    dp = [False] * n
    dp[0] = True 
    for i in range(1, n):
        temp = [False] * n  
        for j in range(i):
            k = stones[i] - stones[j]
            if k <= i:
                temp[k] = dp[k - 1] or dp[k] or dp[k + 1]

        dp = temp 
    return any(dp)

n = int(input())
stones = list(map(int, input().split()))

result = can_cross_river(n, stones)
print(result)