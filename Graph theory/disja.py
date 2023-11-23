import heapq

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        adj = {str(i): [] for i in range(n_vertices)}
        while True:
            a, b, w = map(str, input().split())
            if a == "-1":
                break
            w = int(w)
            adj[a].append((b, w))
            adj[b].append((a, w))
        self.adj = adj

    def dijkstra(self, start):
        adj = self.adj
        n_vertices = self.n_vertices
        d = {str(i): float('inf') for i in range(n_vertices)}
        visited = {str(i): False for i in range(n_vertices)}
        d[start] = 0
        Q = [(0, start)]
        heapq.heapify(Q)

        while Q:
            _, u = heapq.heappop(Q)

            if visited[u]:
                continue

            visited[u] = True

            for item in adj[u]:
                v, w = item
                if not visited[v] and d[v] > w + d[u]:
                    d[v] = w + d[u]
                    heapq.heappush(Q, (d[v], v))

        print("\n".join(str(item) for item in d.values()))

def solution():
    n_vertices = int(input())
    g = Graph(n_vertices)
    start = input()
    g.dijkstra(start)

if __name__ == "__main__":
    solution()
