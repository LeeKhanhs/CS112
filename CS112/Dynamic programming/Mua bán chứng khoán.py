def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    profit = [0] * n

    max_sell_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_sell_price = max(max_sell_price, prices[i])
        profit[i] = max(profit[i + 1], max_sell_price - prices[i])

    min_buy_price = prices[0]
    for i in range(1, n):
        min_buy_price = min(min_buy_price, prices[i])
        profit[i] = max(profit[i - 1], profit[i] + prices[i] - min_buy_price)

    return profit[-1]

n = int(input())
prices = list(map(int, input().split()))

result = maxProfit(prices)
print(result)