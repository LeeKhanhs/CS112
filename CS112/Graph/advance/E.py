def tarjan_scc(n, a, cost):
    global num, low, time, st, deleted, ans_cost, ans_cnt
    time += 1
    num[n] = low[n] = time
    st.append(n)
    for v in a[n]:
        if deleted[v]:
            continue
        if num[v] != 0:
            low[n] = min(low[n], num[v])
        else:
            tarjan_scc(v, a, cost)
            low[n] = min(low[n], low[v])

    # Find minimum cost and count of minimum cost in each SCC
    if num[n] == low[n]:
        min_cost = cost[n]
        cnt_min_cost = 0
        while st:
            v = st.pop()
            deleted[v] = True
            if cost[v] < min_cost:
                min_cost = cost[v]
                cnt_min_cost = 1
            elif cost[v] == min_cost:
                cnt_min_cost += 1
            if n == v:
                break

        ans_cost += min_cost  # Choose the planet with minimum cost in each SCC
        ans_cnt = (ans_cnt * cnt_min_cost) % 1000000007  # If there are more than one planet with minimum cost, choose any one

n = int(input())
cost = [0] + list(map(int, input().split()))
m = int(input())
a = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)

num = [0] * (n + 1)
low = [0] * (n + 1)
deleted = [False] * (n + 1)
time = 0
st = []
ans_cost = 0  # Minimum cost
ans_cnt = 1  # Count of minimum cost

for i in range(1, n + 1):
    if num[i] == 0:
        tarjan_scc(i, a, cost)

print(ans_cost, ans_cnt % 1000000007)