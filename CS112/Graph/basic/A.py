class Graph:
    def __init__(self, n):
        adj = {}
        vertexs = []

        for i in range(n):
            a, b = map(str, input().split())
            if a not in vertexs:
                vertexs.append(a)
                adj.setdefault(a, [])
            if b not in vertexs:
                vertexs.append(b)
                adj.setdefault(b, [])
            

            adj[a].append(b)
            adj[b].append(a)

        visited = {vertex: False for vertex in vertexs}

        self.adj = adj
        self.visited = visited
        self.vertexs = vertexs

    def dfs(self, start):
        self.visited[start] = True
        print(start, end=" ")
        for u in self.adj[start]:
            if not self.visited[u]:
                self.dfs(u)

    def bfs(self, start):
        self.visited = {vertex: False for vertex in self.vertexs}
        q = [start]
        while q:
            s = q.pop(0)
            print(s, end=" ")
            self.visited[s] = True
            for u in self.adj[s]:
                if not self.visited[u]:
                    q.append(u)
                    self.visited[u] = True
def solution(n_tests):
    for _ in range(n_tests):
        n = int(input())
        g = Graph(n)
        v = input().strip()
        
        print("DFS:")
        g.dfs(v)
        print("\nBFS:")
        g.bfs(v)
        print("\n")
        
        
if __name__ == "__main__":
    n_tests = int(input())
    solution(n_tests)