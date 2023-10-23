# input
n, K = map(int, input().split())
items = []
for _ in range(n):
    m, v = map(int, input().split())
    items.append([m, v])

# check
def check(items, K, p):
    global n
    items_ratio = [items[i][1] - p*items[i][0] for i in range(n)] # Chứng minh
    items_ratio = sorted(items_ratio, reverse=True)
    total = sum(items_ratio[:K])
    # print(items_ratio)
    return total >= 0

# binary search
left, right = 0, max([x[1] / x[0] for x in items]) # chứng minh
# lưu ý cần tìm p lớn
while left <= right:
    p_check = int((left + right) / 2)
    
    if check(items, K, p_check):
        left = p_check + 1
        final= p_check
    else:
        right = p_check - 1
    
print(final)