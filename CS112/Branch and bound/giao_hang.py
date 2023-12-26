def find_shortest_time(n, m, roads):
    graph = {i: {} for i in range(1, n + 1)}

    for road in roads:
        u, v, w = road
        graph[u][v] = w
        graph[v][u] = w

    def backtrack(path, visited, current_time, current_node):
        nonlocal shortest_time

        if len(path) == n:
            shortest_time = min(shortest_time, current_time)
            return

        for neighbor, weight in graph[current_node].items():
            if not visited[neighbor]:
                visited[neighbor] = True
                backtrack(path + [neighbor], visited, current_time + weight, neighbor)
                visited[neighbor] = False

    shortest_time = float('inf')
    start_node = 1
    visited = [False] * (n + 1)
    visited[start_node] = True

    backtrack([start_node], visited, 0, start_node)

    if shortest_time == float('inf'):
        print("-1")
    else:
        print(shortest_time)


n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

find_shortest_time(n, m, roads)