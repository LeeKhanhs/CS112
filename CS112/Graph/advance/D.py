import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, n, m):
        self.adj = {f"{i + 1}": [] for i in range(n)}  # dictionary vertex
        self.visited = {f"{i + 1}": 0 for i in range(n)}  # dictionary status vertex
        self.cycle = False # check cycle

        # input
        for i in range(m):
            a, b = map(str, input().split())
            self.adj[a].append(b)
    
    
    # Intergate all the vertex, dfs each vertex, if this vertex is visted at leaste 2 time -> has cycle
    def dfs(self, u):
        self.visited[u] = 1
        for v in self.adj[u]:
            if self.visited[v] == 0:
                self.dfs(v)
            elif self.visited[v] == 1:
                self.cycle = True

        self.visited[u] = 2

    def detect_cycle(self):
        for u in self.adj:
            if self.visited[u] == 0:
                self.dfs(u)



def solution():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        g = Graph(n, m)
        g.detect_cycle()
        if g.cycle:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solution()